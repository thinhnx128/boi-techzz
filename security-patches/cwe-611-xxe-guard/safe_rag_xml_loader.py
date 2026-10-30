"""
Remediates CWE-611 XML External Entity (XXE) Injection in RAG Document Loaders.
Rejects DOCTYPE / ENTITY declarations prior to XML parsing.
"""
import xml.etree.ElementTree as ET


def safe_parse_rag_xml(xml_content: str) -> ET.Element:
    upper = xml_content.upper()
    if "<!DOCTYPE" in upper or "<!ENTITY" in upper or "SYSTEM" in upper:
        raise PermissionError("[CWE-611 Guard] Blocked XML DTD / External Entity (XXE) declaration")
    return ET.fromstring(xml_content)
