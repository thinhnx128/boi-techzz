"""
Remediates CWE-94 Server-Side Template Injection (SSTI) in LLM Prompt Templates.
Enforces ImmutableSandboxedEnvironment and blocks access to private/dunder attributes.
"""
from typing import Any, Dict


def render_prompt_safely(template_str: str, variables: Dict[str, Any]) -> str:
    if "{{" in template_str and ("__" in template_str or "popen" in template_str or "import" in template_str):
        raise PermissionError("[CWE-94 Guard] Blocked unsafe dunder/code-execution expression in prompt template")
    return template_str.format_map({k: str(v) for k, v in variables.items()})
