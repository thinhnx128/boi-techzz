## Security Fix: Prevent Arbitrary Code Execution via Unsafe Pickle Deserialization (CWE-502)
- **Vulnerability:** CWE-502 (Deserialization of Untrusted Data)
- **Impact:** Loading untrusted checkpoint metadata via `pickle.loads()` allows arbitrary OS command execution via crafted `__reduce__` opcodes.
- **Fix:** Replaced raw `pickle.loads()` with `SafeCheckpointUnpickler` enforcing a strict `(module, class)` allowlist.