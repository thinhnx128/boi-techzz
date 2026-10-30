# 🛡️ Huntr.com & GitHub Security Advisory — 4-CWE AI/ML Guardrail Suite (@thinhnx128)

## Covered CWE Classes & Ready-to-Submit PoCs
1. **CWE-502**: Unsafe Deserialization (`pickle.loads`, `torch.load` without `weights_only=True`, `yaml.unsafe_load`) -> Fixed via `SafeUnpickler` allowlist.
2. **CWE-78**: OS Command Injection in AI Agent tool execution (`subprocess` with `shell=True`, `eval`) -> Fixed via `safe_agent_subprocess` & `ast.literal_eval`.
3. **CWE-918**: Server-Side Request Forgery (SSRF) against Cloud Metadata (`169.254.169.254`) -> Fixed via `validate_url_no_ssrf` DNS/IP validator.
4. **CWE-22**: Arbitrary File Overwrite / ZipSlip during model archive extraction -> Fixed via `safe_extract_tar` canonical path containment check.
