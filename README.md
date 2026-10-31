# `@thinhnx128/boi-tech-ai-security-sdk` (`boi-techzz`)

Defensive AI/LLM Guardrail & Security Remediation Suite maintained by **Xuan Thinh Nguyen ([`@thinhnx128`](https://github.com/thinhnx128))**.

- **Latest Patched Release**: [`v1.0.1`](https://github.com/thinhnx128/boi-techzz/releases/tag/v1.0.1) ([CalVer `v2026.10.30`](https://github.com/thinhnx128/boi-techzz/releases/tag/v2026.10.30))
- **Initial Affected Baseline**: [`v1.0.0`](https://github.com/thinhnx128/boi-techzz/releases/tag/v1.0.0) (`< 1.0.1`)
- **Security Advisories**: [10 Published GHSA Advisories](https://github.com/thinhnx128/boi-techzz/security/advisories) (see [`SECURITY.md`](./SECURITY.md) and [`CHANGELOG.md`](./CHANGELOG.md))

## Remediated Modules (`security-patches/`)

1. `security-patches/cwe-502-safe-loader/safe_checkpoint_loader.py` — Restricted `pickle.Unpickler` & HMAC-SHA256 verification (`GHSA-p49q-3f4w-j672`, `CWE-502`)
2. `security-patches/cwe-78-safe-executor/safe_tool_executor.py` — Binary allowlisting & `shell=False` enforcement (`GHSA-3x2g-xg34-42pq`, `CWE-78`)
3. `security-patches/cwe-918-ssrf-guard/safe_rag_url_fetcher.py` — DNS/IP validation blocking `169.254.169.254` & RFC1918 ranges (`GHSA-p4rc-37fp-fvv2`, `CWE-918`)
4. `security-patches/cwe-22-zipslip-guard/safe_archive_extractor.py` — Canonical path containment check during archive extraction (`GHSA-x9x3-4qrj-g4hx`, `CWE-22`)
5. `security-patches/cwe-94-ssti-guard/sandboxed_prompt_renderer.py` — Sandboxed prompt template rendering (`GHSA-pg2c-5pwj-58r2`, `CWE-94`)
6. `security-patches/cwe-89-sql-guard/safe_text2sql_executor.py` — Single-statement `SELECT` enforcement for Text-to-SQL agents (`GHSA-hff2-r3gp-j4jv`, `CWE-89`)
7. `security-patches/cwe-611-xxe-guard/safe_rag_xml_loader.py` — XML DTD & external entity blocker for RAG ingestion (`GHSA-wrc3-8c98-283w`, `CWE-611`)
8. `security-patches/cwe-79-xss-guard/safe_markdown_renderer.ts` — Stored XSS sanitizer for LLM Markdown/HTML output (`GHSA-vr42-692h-pmm6`, `CWE-79`)
9. `security-patches/cwe-532-log-redactor/secret_log_redactor.py` — Telemetry Bearer/API key redactor (`GHSA-q749-wr8p-6pc9`, `CWE-532`)
10. `security-patches/cwe-1333-redos-guard/safe_llm_output_parser.py` — Linear-time `O(N)` LLM JSON code-block parser (`GHSA-q77q-crp2-mmjc`, `CWE-1333`)
