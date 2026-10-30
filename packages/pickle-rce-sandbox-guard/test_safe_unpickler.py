# File: security_patch/test_safe_unpickler.py
import os
import pickle
import pytest
from safe_unpickler import safe_pickle_loads, UnsafePickleError

class MaliciousRCEPayload:
    def __reduce__(self):
        return (os.system, ("echo PWNED",))

def test_blocks_malicious_rce_pickle_payload():
    malicious_bytes = pickle.dumps(MaliciousRCEPayload())
    with pytest.raises(UnsafePickleError, match="Blocked CWE-502 RCE attempt"):
        safe_pickle_loads(malicious_bytes)

def test_allows_safe_dictionary_metadata():
    safe_bytes = pickle.dumps({"epoch": 12, "loss": 0.034, "tags": ["v1", "prod"]})
    restored = safe_pickle_loads(safe_bytes)
    assert restored["epoch"] == 12