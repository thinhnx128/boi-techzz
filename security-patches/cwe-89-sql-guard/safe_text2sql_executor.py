"""
Remediates CWE-89 SQL Injection in Text-to-SQL AI Agents.
Rejects stacked queries, DDL/DML keywords, and system functions before execution.
"""
import re

FORBIDDEN_SQL_PATTERNS = re.compile(
    r"\b(DROP|DELETE|UPDATE|INSERT|ALTER|GRANT|TRUNCATE|COPY|pg_read_file|xp_cmdshell|INTO\s+OUTFILE)\b",
    re.IGNORECASE,
)


def validate_readonly_sql(sql_query: str) -> str:
    cleaned = sql_query.strip().rstrip(";")
    if ";" in cleaned:
        raise PermissionError("[CWE-89 Guard] Stacked multi-statement SQL queries are forbidden")
    if not cleaned.upper().startswith("SELECT "):
        raise PermissionError("[CWE-89 Guard] Only single SELECT queries are allowed in Text-to-SQL Agent")
    if FORBIDDEN_SQL_PATTERNS.search(cleaned):
        raise PermissionError("[CWE-89 Guard] Blocked dangerous SQL keyword/function in generated query")
    return cleaned
