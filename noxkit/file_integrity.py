import hashlib


def generate_file_hash(file_data):
    try:
        return hashlib.sha256(file_data).hexdigest()

    except (TypeError, ValueError):
        return None