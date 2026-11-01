# Open-Source AI & Cloud Security Advisories (CVE / GHSA / CWE Research)

This repository contains technical root-cause analyses, MITRE CVE JSON 5.1 records, and reference defensive patches for security vulnerabilities (`CWE` / `CVE` / `GHSA`) in open-source AI, LLM, RAG, MCP, and WebAssembly ecosystems.

## Repository Structure (CVE Disclosure Scope Only)

- [`cve-reports/`](./cve-reports): Technical vulnerability advisories, MITRE CVE 5.1 JSON descriptors, CVSS v3.1 vectors, and unified defensive diffs (`CWE-22`, `CWE-78`, `CWE-352`, `CWE-400`, `CWE-502`, `CWE-918`).
- [`security-patches/`](./security-patches): Reference defensive guards for 10 critical CWE classes (`CWE-22`, `CWE-78`, `CWE-79`, `CWE-89`, `CWE-94`, `CWE-502`, `CWE-532`, `CWE-611`, `CWE-918`, `CWE-1333`).
- [`packages/ai-cwe-guardrail-suite/`](./packages/ai-cwe-guardrail-suite): Huntr & GHSA multi-CWE security guardrail suite.
- [`packages/pickle-rce-sandbox-guard/`](./packages/pickle-rce-sandbox-guard): Safe checkpoint unpickler mitigating `CWE-502` deserialization.
- [`packages/rag-security-ssrf-patch/`](./packages/rag-security-ssrf-patch): Safe RAG URL loader mitigating `CWE-918` SSRF & DNS Rebinding.
- [`packages/javelin-integrity-sha256-4/`](./packages/javelin-integrity-sha256-4): Cryptographic SHA-256 integrity verifier mitigating `CWE-328` weak CRC32.
- [`SECURITY.md`](./SECURITY.md): Coordinated Vulnerability Disclosure (CVD) policy.
