import hashlib
from typing import Optional


def generate_file_hash(file_data: bytes) -> Optional[str]:

    """Generates a SHA-256 hash for the given file data."""
    
    try:
        return hashlib.sha256(file_data).hexdigest()

    except (TypeError, ValueError):
        return None