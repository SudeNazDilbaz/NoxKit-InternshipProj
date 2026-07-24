import hashlib

from noxkit.hash_generator import generate_hash

TEST_TEXT = "hello"

EXPECTED_RESULTS = {
    "MD5": hashlib.md5(TEST_TEXT.encode()).hexdigest(),
    "SHA-1": hashlib.sha1(TEST_TEXT.encode()).hexdigest(),
    "SHA-256": hashlib.sha256(TEST_TEXT.encode()).hexdigest(),
    "SHA-512": hashlib.sha512(TEST_TEXT.encode()).hexdigest(),
}


print("=" * 50)
print("Hash Generator Test Results")
print("=" * 50)


for algorithm, expected_hash in EXPECTED_RESULTS.items():
    actual_hash = generate_hash(TEST_TEXT, algorithm)

    assert actual_hash == expected_hash, (
        f"Test failed for {algorithm}: "
        f"expected {expected_hash}, got {actual_hash}"
    )

    print(f"PASS: {algorithm}")
    print(f"Hash: {actual_hash}\n")


unsupported_result = generate_hash(TEST_TEXT, "SHA-999")

assert unsupported_result is None, (
    "Unsupported algorithm test failed: expected None"
)

print("PASS: Unsupported algorithm returns None")
print("\nAll Hash Generator tests passed successfully.")