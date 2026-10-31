# Security Policy & Coordinated Vulnerability Disclosure (`@thinhnx128/boi-tech-ai-security-sdk`)

## Supported Versions

| Version | Release Tag | Status | Security Notes |
| :--- | :--- | :--- | :--- |
| **`1.0.1`** (`2026.10.30`) | [`v1.0.1`](https://github.com/thinhnx128/boi-techzz/releases/tag/v1.0.1) | ✅ **Supported (Patched)** | Remediates all 10 published `GHSA` / `CWE` advisories (PRs `#1`–`#10` merged into `main`). |
| **`1.0.0`** (`2026.10.0`) | [`v1.0.0`](https://github.com/thinhnx128/boi-techzz/releases/tag/v1.0.0) | ❌ **Affected (`< 1.0.1`)** | Initial baseline containing unpatched AI Agent, RAG, and LLM parsing modules. |

---

## Published Security Advisories & Remediation Matrix (`v1.0.1`)

| # | GHSA ID | MITRE / CNA Ref | CWE | CVSS v3.1 | Affected | Patched | Merged PR | Merge Commit SHA |
| :-: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | [`GHSA-p49q-3f4w-j672`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-p49q-3f4w-j672) | `CAN-2026-2041209` | `CWE-502` | **9.8** | `< 1.0.1` | `1.0.1` | [PR #1](https://github.com/thinhnx128/boi-techzz/pull/1) | [`22f77e9`](https://github.com/thinhnx128/boi-techzz/commit/22f77e93f44fdfeaa7cfccf7ec3fe3ae11e49556) |
| 2 | [`GHSA-3x2g-xg34-42pq`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-3x2g-xg34-42pq) | `CAN-2026-2041211` | `CWE-78` | **9.8** | `< 1.0.1` | `1.0.1` | [PR #2](https://github.com/thinhnx128/boi-techzz/pull/2) | [`a964d51`](https://github.com/thinhnx128/boi-techzz/commit/a964d5181d865a7d773538223f2e6da4dd2f8c58) |
| 3 | [`GHSA-p4rc-37fp-fvv2`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-p4rc-37fp-fvv2) | `CAN-2026-2041213` | `CWE-918` | **9.3** | `< 1.0.1` | `1.0.1` | [PR #3](https://github.com/thinhnx128/boi-techzz/pull/3) | [`c681c95`](https://github.com/thinhnx128/boi-techzz/commit/c681c95af07df93ce3fbbe5180ca994570f381f3) |
| 4 | [`GHSA-x9x3-4qrj-g4hx`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-x9x3-4qrj-g4hx) | `CAN-2026-2041214` | `CWE-22` | **8.8** | `< 1.0.1` | `1.0.1` | [PR #4](https://github.com/thinhnx128/boi-techzz/pull/4) | [`a352fc0`](https://github.com/thinhnx128/boi-techzz/commit/a352fc0e12936c6117b5dc2d07c7058283ec980c) |
| 5 | [`GHSA-pg2c-5pwj-58r2`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-pg2c-5pwj-58r2) | `GitHub CNA 202` | `CWE-94` | **9.8** | `< 1.0.1` | `1.0.1` | [PR #5](https://github.com/thinhnx128/boi-techzz/pull/5) | [`60c0fee`](https://github.com/thinhnx128/boi-techzz/commit/60c0feea1120b21fe64bfb073d6b20e78689e308) |
| 6 | [`GHSA-hff2-r3gp-j4jv`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-hff2-r3gp-j4jv) | `GitHub CNA 202` | `CWE-89` | **9.8** | `< 1.0.1` | `1.0.1` | [PR #6](https://github.com/thinhnx128/boi-techzz/pull/6) | [`3ba6a6c`](https://github.com/thinhnx128/boi-techzz/commit/3ba6a6c48d0e5458a0a04cfb7e8d185538222925) |
| 7 | [`GHSA-wrc3-8c98-283w`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-wrc3-8c98-283w) | `GitHub CNA 202` | `CWE-611` | **8.6** | `< 1.0.1` | `1.0.1` | [PR #7](https://github.com/thinhnx128/boi-techzz/pull/7) | [`04fbdda`](https://github.com/thinhnx128/boi-techzz/commit/04fbddae0c471964b2e4f304993739a84229b11c) |
| 8 | [`GHSA-vr42-692h-pmm6`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-vr42-692h-pmm6) | `GitHub CNA 202` | `CWE-79` | **8.2** | `< 1.0.1` | `1.0.1` | [PR #8](https://github.com/thinhnx128/boi-techzz/pull/8) | [`1d64201`](https://github.com/thinhnx128/boi-techzz/commit/1d64201f90512e62cfae1ca455d2707989b7c7f1) |
| 9 | [`GHSA-q749-wr8p-6pc9`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-q749-wr8p-6pc9) | `GitHub CNA 202` | `CWE-532` | **8.5** | `< 1.0.1` | `1.0.1` | [PR #9](https://github.com/thinhnx128/boi-techzz/pull/9) | [`98cb9b5`](https://github.com/thinhnx128/boi-techzz/commit/98cb9b502c096ad81338dfce7ce6efa8ef68df2a) |
| 10 | [`GHSA-q77q-crp2-mmjc`](https://github.com/thinhnx128/boi-techzz/security/advisories/GHSA-q77q-crp2-mmjc) | `GitHub CNA 202` | `CWE-1333` | **7.5** | `< 1.0.1` | `1.0.1` | [PR #10](https://github.com/thinhnx128/boi-techzz/pull/10) | [`f625a28`](https://github.com/thinhnx128/boi-techzz/commit/f625a28a0e79c08f57689704b293727dd8c3197c) |

## Reporting a Vulnerability

Please report security issues via [GitHub Security Advisories](https://github.com/thinhnx128/boi-techzz/security/advisories/new).
