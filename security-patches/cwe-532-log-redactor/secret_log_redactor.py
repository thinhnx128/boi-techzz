"""
Remediates CWE-532 Sensitive API Key & Token Exposure in AI Agent Logs.
Automatically redacts Bearer tokens, sk-* keys, and ghp_* tokens before logging.
"""
import re

SECRET_PATTERNS = re.compile(
    r"(Bearer\s+[A-Za-z0-9_\-\.]+|sk-[A-Za-z0-9_\-]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})",
    re.IGNORECASE,
)


def redact_sensitive_log(message: str) -> str:
    return SECRET_PATTERNS.sub("[REDACTED_SECRET_CWE_532]", message)
