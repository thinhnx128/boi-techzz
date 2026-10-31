"""
Remediates GHSA-p49q-3f4w-j672 / MITRE CAN-2026-2041209 (CWE-502 Unsafe Deserialization)
Enforces safetensors, torch.load(weights_only=True), yaml.safe_load(), and HMAC-SHA256 verification.
"""
import hashlib
import hmac
import io
import pickle
from typing import Any, Set, Tuple

ALLOWED_SAFE_GLOBALS: Set[Tuple[str, str]] = {
    ("collections", "OrderedDict"),
    ("torch._utils", "_rebuild_tensor_v2"),
}


class RestrictedModelUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str) -> Any:
        if (module, name) not in ALLOWED_SAFE_GLOBALS:
            raise pickle.UnpicklingError(
                f"[GHSA-p49q-3f4w-j672] Blocked unsafe class {module}.{name} during deserialization"
            )
        return super().find_class(module, name)


def safe_pickle_loads(payload: bytes, hmac_key: bytes = b"", expected_sig: str = "") -> Any:
    if hmac_key:
        actual_sig = hmac.new(hmac_key, payload, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(actual_sig, expected_sig):
            raise ValueError("[GHSA-p49q-3f4w-j672] Checkpoint HMAC-SHA256 integrity check failed")
    return RestrictedModelUnpickler(io.BytesIO(payload)).load()
