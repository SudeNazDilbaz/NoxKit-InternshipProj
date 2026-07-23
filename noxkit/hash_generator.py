import hashlib
from typing import Callable

HASH_ALGORITHMS: dict[str, Callable] = {
    "md5": hashlib.md5,
    "sha1":  hashlib.sha1,
    "sha256":  hashlib.sha256,
    "sha512":  hashlib.sha512,
}

def generate_hash(text:str,algorithm:str) -> str | None:
    
    """Generates a hash value for the given text,using a selected algorithm."""

    normalized_algorithms = algorithm.lower().replace("-", "")
    hash_function = HASH_ALGORITHMS.get(normalized_algorithms)

    if hash_function is None:
        return None

    return hash_function(text.encode()).hexdigest()