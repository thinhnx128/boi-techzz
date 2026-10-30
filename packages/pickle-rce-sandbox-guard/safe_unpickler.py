# File: security_patch/safe_unpickler.py
import io
import pickle
from typing import Any

ALLOWED_MODULES = {
    'builtins': {'dict', 'list', 'tuple', 'set', 'frozenset', 'int', 'float', 'str', 'bytes', 'bool'},
    'collections': {'OrderedDict', 'defaultdict'},
}

class UnsafePickleError(Exception):
    """Raised when a pickle payload attempts to import unauthorized globals (CWE-502 RCE)."""
    pass

class SafeCheckpointUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str) -> Any:
        allowed_names = ALLOWED_MODULES.get(module)
        if allowed_names is not None and name in allowed_names:
            return super().find_class(module, name)
        raise UnsafePickleError(
            f"Blocked CWE-502 RCE attempt: forbidden global '{module}.{name}' in pickle stream"
        )

def safe_pickle_loads(data: bytes) -> Any:
    return SafeCheckpointUnpickler(io.BytesIO(data)).load()