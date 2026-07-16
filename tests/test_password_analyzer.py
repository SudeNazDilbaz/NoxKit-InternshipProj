from noxkit.password_analyzer import analyze_password

passwords = [
    "password",
    "Password",
    "Password123",
    "Password123!",
    "12345678",
    "abc",
]

print("=" * 50)
print("Password Analyzer Test Results")
print("=" * 50)

for password in passwords:
    result = analyze_password(password)
    print(f"{password} -> {result}")

print("\nAll tests completed.")