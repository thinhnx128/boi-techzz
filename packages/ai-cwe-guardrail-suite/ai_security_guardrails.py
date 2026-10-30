# File: packages/ai-cwe-guardrail-suite/ai_security_guardrails.py
# Unified Remediation Suite for the Top 4 AI/ML Security Vulnerabilities:
#   1. CWE-502: Unsafe Deserialization (pickle.loads, torch.load, yaml.unsafe_load)
#   2. CWE-78:  OS Command Injection in AI Agent Tool Execution (subprocess shell=True, eval)
#   3. CWE-918: Server-Side Request Forgery (SSRF) against Cloud Metadata (169.254.169.254)
#   4. CWE-22:  Arbitrary File Overwrite / ZipSlip during Model Archive Extraction
# Author: Xuan Thinh (@thinhnx128) <thinhnx128@gmail.com>

import ast
import io
import ipaddress
import pickle
import socket
import subprocess
import tarfile
import zipfile
from pathlib import Path
from typing import Any, Sequence
from urllib.parse import urlparse

class SecurityGuardrailViolation(Exception):
    """Raised when an AI/ML security guardrail blocks an exploit payload (CWE-502 / CWE-78 / CWE-918 / CWE-22)."""
    pass

# ============================================================================
# 1. CWE-502: Safe Deserialization Guard (Blocks Pickle RCE & Unsafe Torch Load)
# ============================================================================
ALLOWED_PICKLE_GLOBALS = {
    "builtins": {"dict", "list", "tuple", "set", "frozenset", "int", "float", "str", "bytes", "bool"},
    "collections": {"OrderedDict", "defaultdict"},
}

class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str) -> Any:
        allowed = ALLOWED_PICKLE_GLOBALS.get(module)
        if allowed is not None and name in allowed:
            return super().find_class(module, name)
        raise SecurityGuardrailViolation(
            f"[CWE-502 Blocked] Forbidden global '{module}.{name}' in pickle stream."
        )

def safe_pickle_loads(payload: bytes) -> Any:
    return SafeUnpickler(io.BytesIO(payload)).load()

# ============================================================================
# 2. CWE-78: Safe AI Agent Tool Command & Expression Executor
# ============================================================================
ALLOWED_AGENT_BINARIES = {"git", "ls", "cat", "grep", "find", "python3", "node"}

def safe_agent_subprocess(argv: Sequence[str], timeout_sec: int = 15) -> subprocess.CompletedProcess:
    if not argv or not isinstance(argv, (list, tuple)):
        raise SecurityGuardrailViolation("[CWE-78 Blocked] Command must be a non-empty argument list (shell=False).")
    binary = Path(argv[0]).name
    if binary not in ALLOWED_AGENT_BINARIES:
        raise SecurityGuardrailViolation(f"[CWE-78 Blocked] Binary '{binary}' is not in ALLOWED_AGENT_BINARIES.")
    for arg in argv[1:]:
        if any(ch in arg for ch in (";", "|", "&", "`", "$(")):
            raise SecurityGuardrailViolation(f"[CWE-78 Blocked] Shell metacharacter detected in argument: {arg!r}")
    return subprocess.run(list(argv), shell=False, capture_output=True, text=True, timeout=timeout_sec, check=False)

def safe_agent_eval(expr: str) -> Any:
    """Replaces dangerous eval() with AST-validated literal/arithmetic evaluation (CWE-78)."""
    try:
        return ast.literal_eval(expr)
    except (ValueError, SyntaxError) as exc:
        raise SecurityGuardrailViolation(f"[CWE-78 Blocked] Unsafe expression rejected by ast.literal_eval: {exc}") from exc

# ============================================================================
# 3. CWE-918: Cloud Metadata & Internal Network SSRF Guard (169.254.169.254)
# ============================================================================
def validate_url_no_ssrf(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise SecurityGuardrailViolation(f"[CWE-918 Blocked] Disallowed URL scheme '{parsed.scheme}'.")
    hostname = parsed.hostname
    if not hostname:
        raise SecurityGuardrailViolation("[CWE-918 Blocked] URL missing hostname.")
    if hostname.lower() in ("localhost", "metadata.google.internal", "169.254.169.254"):
        raise SecurityGuardrailViolation(f"[CWE-918 Blocked] Forbidden internal/metadata host '{hostname}'.")

    addr_info = socket.getaddrinfo(hostname, parsed.port or (443 if parsed.scheme == "https" else 80))
    for entry in addr_info:
        ip_str = entry[4][0]
        ip_obj = ipaddress.ip_address(ip_str)
        if (
            ip_obj.is_private
            or ip_obj.is_loopback
            or ip_obj.is_link_local
            or ip_obj.is_multicast
            or ip_obj.is_reserved
            or str(ip_obj) == "169.254.169.254"
        ):
            raise SecurityGuardrailViolation(
                f"[CWE-918 Blocked] Host '{hostname}' resolved to internal/cloud metadata IP {ip_str}."
            )
    return url

# ============================================================================
# 4. CWE-22: Safe Model Archive Extractor (Blocks ZipSlip & Symlink Escape)
# ============================================================================
def safe_extract_tar(tar: tarfile.TarFile, dest_dir: str | Path) -> list[Path]:
    base_dir = Path(dest_dir).resolve()
    extracted: list[Path] = []
    for member in tar.getmembers():
        if member.issym() or member.islnk():
            raise SecurityGuardrailViolation(f"[CWE-22 Blocked] Symlink/hardlink entry forbidden: {member.name}")
        target_path = (base_dir / member.name).resolve()
        if not target_path.is_relative_to(base_dir):
            raise SecurityGuardrailViolation(f"[CWE-22 Blocked] ZipSlip path traversal detected: {member.name}")
    tar.extractall(path=base_dir)
    return extracted
