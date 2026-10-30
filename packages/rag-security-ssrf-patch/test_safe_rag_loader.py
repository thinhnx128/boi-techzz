# File: security_patch/test_safe_rag_loader.py
import pytest
from safe_rag_loader import validate_public_url, SecurityViolationError

def test_blocks_aws_cloud_metadata_ssrf():
    with pytest.raises(SecurityViolationError, match="SSRF Blocked"):
        validate_public_url("http://169.254.169.254/latest/meta-data/iam/security-credentials/")

def test_blocks_localhost_loopback_ssrf():
    with pytest.raises(SecurityViolationError, match="SSRF Blocked"):
        validate_public_url("http://127.0.0.1:8080/admin/config")

def test_blocks_file_scheme():
    with pytest.raises(SecurityViolationError, match="unsafe URL scheme"):
        validate_public_url("file:///etc/passwd")