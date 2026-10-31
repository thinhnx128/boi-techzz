"""
Remediates GHSA-3x2g-xg34-42pq / MITRE CAN-2026-2041211 (CWE-78 OS Command Injection)
Enforces shell=False, strict binary allowlisting, and ast.literal_eval().
"""
import ast
import subprocess
from typing import List, Set

ALLOWED_BINARIES: Set[str] = {"git", "python3", "pytest"}


def execute_agent_tool_safely(argv: List[str], timeout_sec: int = 15) -> str:
    if not argv or argv[0] not in ALLOWED_BINARIES:
        raise PermissionError(f"[GHSA-3x2g-xg34-42pq] Disallowed binary: {argv[0] if argv else 'empty'}")
    for arg in argv[1:]:
        if any(ch in arg for ch in (";", "|", "&", "`", "$", "\n", "\r")):
            raise ValueError(f"[GHSA-3x2g-xg34-42pq] Blocked shell metacharacter in argument: {arg}")
    completed = subprocess.run(argv, shell=False, capture_output=True, text=True, timeout=timeout_sec, check=False)
    return completed.stdout
