import re
from typing import Any


def analyze_password(password:str) -> dict[str,Any]:

    """Analyzes the given password according to common criteria."""
    
    checks = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    score = sum(checks.values())

    return {
        "checks": checks,
        "score": score,
    }