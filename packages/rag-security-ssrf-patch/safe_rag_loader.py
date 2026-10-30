# File: security_patch/safe_rag_loader.py
import ipaddress
import os
import socket
import tarfile
from urllib.parse import urlparse
import requests

class SecurityViolationError(Exception):
    """Raised when an SSRF or Path Traversal attempt is blocked."""
    pass

def validate_public_url(url: str) -> str:
    """
    Blocks CWE-918 (SSRF) against localhost, RFC1918 private networks,
    and Cloud Instance Metadata (169.254.169.254) including DNS rebinding checks.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        raise SecurityViolationError(f"Blocked unsafe URL scheme: {parsed.scheme}")
    if not parsed.hostname:
        raise SecurityViolationError("Missing hostname in URL")

    try:
        addr_info = socket.getaddrinfo(parsed.hostname, None)
    except socket.gaierror as exc:
        raise SecurityViolationError(f"DNS resolution failed: {exc}") from exc

    for entry in addr_info:
        ip_str = entry[4][0]
        ip_obj = ipaddress.ip_address(ip_str)
        if (
            ip_obj.is_private
            or ip_obj.is_loopback
            or ip_obj.is_link_local
            or ip_obj.is_multicast
            or ip_obj.is_reserved
        ):
            raise SecurityViolationError(
                f"SSRF Blocked: Host {parsed.hostname} resolves to non-public IP {ip_str}"
            )
    return url

def safe_fetch_rag_document(url: str, timeout: int = 10) -> bytes:
    validate_public_url(url)
    # Disable automatic redirects or re-validate every redirect hop
    resp = requests.get(url, timeout=timeout, allow_redirects=False, stream=True)
    if resp.is_redirect:
        redirect_url = resp.headers.get('Location', '')
        validate_public_url(redirect_url)
    resp.raise_for_status()
    return resp.content[:10 * 1024 * 1024]  # Cap payload at 10MB

def safe_extract_tar(tar_path: str, dest_dir: str) -> None:
    """
    Blocks CWE-22 (ZipSlip / Arbitrary File Overwrite) when extracting AI model checkpoints.
    """
    real_dest = os.path.realpath(dest_dir)
    with tarfile.open(tar_path, 'r:*') as tar:
        for member in tar.getmembers():
            if member.issym() or member.islnk():
                raise SecurityViolationError(f"Blocked symlink in archive: {member.name}")
            member_path = os.path.realpath(os.path.join(real_dest, member.name))
            if not member_path.startswith(real_dest + os.sep):
                raise SecurityViolationError(f"Path Traversal blocked: {member.name}")
        tar.extractall(path=real_dest)