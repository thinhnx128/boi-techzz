## [Feature] Add Integrity Verification (SHA-256 Hash of Executable/Script)

### Summary
Implements SHA-256 integrity verification to detect script/binary tampering at startup as specified in #4:
- Computes SHA-256 of the running script in chunks and compares it in constant time (`hmac.compare_digest`) against `JAVELIN_EXPECTED_SHA256`.
- Performs a guarded exit (`sys.exit(1)`) with diagnostic output when tampering or hash mismatch is detected.
- Includes `pytest` suite verifying both matching hashes and tampered file guarded exit.

### Reference Implementation
https://github.com/thinhnx128/boi-tech-ai-bounties/tree/main/packages/javelin-integrity-sha256-4

/claim #4
Fixes #4