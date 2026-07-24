import hashlib

from noxkit.file_integrity import generate_file_hash


ORIGINAL_FILE_DATA = b"Hello NoxKit"
SAME_FILE_DATA = b"Hello NoxKit"
MODIFIED_FILE_DATA = b"Hello NoxKit!"


print("=" * 50)
print("File Integrity Checker Test Results")
print("=" * 50)


original_hash = generate_file_hash(ORIGINAL_FILE_DATA)
same_file_hash = generate_file_hash(SAME_FILE_DATA)
modified_file_hash = generate_file_hash(MODIFIED_FILE_DATA)

expected_hash = hashlib.sha256(ORIGINAL_FILE_DATA).hexdigest()


assert original_hash == expected_hash, (
    "SHA-256 calculation test failed."
)

print("PASS: Correct SHA-256 hash generated")


assert original_hash == same_file_hash, (
    "Identical file data produced different hashes."
)

print("PASS: Identical file contents produce the same hash")


assert original_hash != modified_file_hash, (
    "Modified file data produced the same hash."
)

print("PASS: Modified file content produces a different hash")


invalid_result = generate_file_hash("This is not byte data")

assert invalid_result is None, (
    "Invalid input test failed: expected None"
)

print("PASS: Invalid input returns None")


print("\nOriginal hash:")
print(original_hash)

print("\nModified hash:")
print(modified_file_hash)

print("\nAll File Integrity Checker tests passed successfully.")