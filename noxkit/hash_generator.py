import hashlib

def generate_hash(text,algorithm):
    algorithm = algorithm.lower().replace("-", "")
    
    if algorithm=="md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm=="sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm=="sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    elif algorithm=="sha512":
        return hashlib.sha512(text.encode()).hexdigest()