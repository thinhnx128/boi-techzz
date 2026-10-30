# File: packages/ai-cwe-guardrail-suite/test_ai_security_guardrails.py
import io
import os
import pickle
import tarfile
import pytest
from ai_security_guardrails import (
    SecurityGuardrailViolation,
    safe_pickle_loads,
    safe_agent_subprocess,
    safe_agent_eval,
    validate_url_no_ssrf,
    safe_extract_tar,
)

class ExploitPickleRCE:
    def __reduce__(self):
        return (os.system, ("id",))

def test_cwe502_blocks_pickle_rce():
    malicious = pickle.dumps(ExploitPickleRCE())
    with pytest.raises(SecurityGuardrailViolation, match="CWE-502 Blocked"):
        safe_pickle_loads(malicious)

def test_cwe78_blocks_command_injection_and_eval():
    with pytest.raises(SecurityGuardrailViolation, match="CWE-78 Blocked"):
        safe_agent_subprocess(["git", "clone", "https://example.com/repo; rm -rf /"])
    with pytest.raises(SecurityGuardrailViolation, match="CWE-78 Blocked"):
        safe_agent_eval("__import__('os').system('whoami')")

def test_cwe918_blocks_aws_cloud_metadata_ssrf():
    with pytest.raises(SecurityGuardrailViolation, match="CWE-918 Blocked"):
        validate_url_no_ssrf("http://169.254.169.254/latest/meta-data/iam/security-credentials/")
    with pytest.raises(SecurityGuardrailViolation, match="CWE-918 Blocked"):
        validate_url_no_ssrf("http://127.0.0.1:8080/admin")

def test_cwe22_blocks_zipslip_archive_traversal(tmp_path):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        info = tarfile.TarInfo(name="../../etc/cron.d/pwn")
        data = b"* * * * * root id\n"
        info.size = len(data)
        tar.addfile(info, io.BytesIO(data))
    buf.seek(0)
    with tarfile.open(fileobj=buf, mode="r:gz") as tar:
        with pytest.raises(SecurityGuardrailViolation, match="CWE-22 Blocked"):
            safe_extract_tar(tar, tmp_path)
