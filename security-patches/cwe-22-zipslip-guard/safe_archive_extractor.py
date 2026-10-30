"""
Remediates GHSA-x9x3-4qrj-g4hx / MITRE CAN-2026-2041214 (CWE-22 ZipSlip Arbitrary File Overwrite)
Validates canonical target path confinement and rejects symlinks/hardlinks before extraction.
"""
import os
import tarfile


def safe_extract_tar(tar: tarfile.TarFile, dest_dir: str) -> None:
    canonical_dest = os.path.realpath(dest_dir)
    for member in tar.getmembers():
        if member.issym() or member.islnk():
            raise PermissionError(f"[GHSA-x9x3-4qrj-g4hx] Blocked symbolic/hard link in archive: {member.name}")
        target_path = os.path.realpath(os.path.join(canonical_dest, member.name))
        if not target_path.startswith(canonical_dest + os.sep):
            raise PermissionError(f"[GHSA-x9x3-4qrj-g4hx] Blocked ZipSlip path traversal entry: {member.name}")
    tar.extractall(path=canonical_dest, filter="data")
