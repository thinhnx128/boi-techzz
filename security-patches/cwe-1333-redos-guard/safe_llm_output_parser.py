"""
Remediates CWE-1333 ReDoS in LLM Output Code-Block Parsers.
Uses deterministic O(N) string index scanning instead of backtracking regexes.
"""
MAX_LLM_OUTPUT_CHARS = 100_000


def extract_json_block_linear(text: str) -> str:
    if len(text) > MAX_LLM_OUTPUT_CHARS:
        raise ValueError("[CWE-1333 Guard] LLM response exceeds maximum allowed length")
    start_marker = "```json"
    start = text.find(start_marker)
    if start == -1:
        return text.strip()
    content_start = start + len(start_marker)
    end = text.find("```", content_start)
    if end == -1:
        return text[content_start:].strip()
    return text[content_start:end].strip()
