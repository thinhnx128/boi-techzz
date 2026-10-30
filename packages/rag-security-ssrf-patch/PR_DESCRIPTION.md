## Vulnerability Disclosure & Fix Report (Huntr.com / GHSA Format)
- **Vulnerability Type:** CWE-918 (Server-Side Request Forgery - SSRF) & CWE-22 (Improper Limitation of a Pathname to a Restricted Directory / ZipSlip)
- **Severity:** High / Critical (CVSS 8.6)
- **Impact:** An unauthenticated user supplying a document URL to the RAG ingestion endpoint can force the server to query internal cloud metadata services (`http://169.254.169.254/latest/meta-data/`) or internal microservices (`127.0.0.1`), leaking cloud credentials.

### Remediation Included in Patch
1. Added `validate_public_url()` which resolves hostnames via `socket.getaddrinfo()` and rejects all loopback, link-local (`169.254.0.0/16`), and RFC1918 private IP ranges.
2. Disabled unvalidated HTTP redirects to prevent redirect-based SSRF bypasses.
3. Added `safe_extract_tar()` with strict `os.path.realpath` prefix verification and symlink rejection.