"""
Remediates GHSA-p4rc-37fp-fvv2 / MITRE CAN-2026-2041213 (CWE-918 Cloud Metadata SSRF)
Blocks RFC1918, loopback, and link-local 169.254.169.254 IPs before HTTP connection.
"""
import ipaddress
import socket
from urllib.parse import urlparse


def validate_public_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("[GHSA-p4rc-37fp-fvv2] Only http/https URLs with valid hostnames are permitted")
    for res in socket.getaddrinfo(parsed.hostname, None):
        ip_obj = ipaddress.ip_address(res[4][0])
        if (
            ip_obj.is_private
            or ip_obj.is_loopback
            or ip_obj.is_link_local
            or ip_obj.is_multicast
            or ip_obj.is_reserved
        ):
            raise PermissionError(f"[GHSA-p4rc-37fp-fvv2] Blocked internal/metadata IP address: {ip_obj}")
    return url
