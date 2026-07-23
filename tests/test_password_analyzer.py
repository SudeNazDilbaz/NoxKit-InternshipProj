from noxkit.password_analyzer import analyze_password

test_cases ={
    "password":2,
    "Password":3,
    "Password123":4,
    "Password123!":5,
    "12345678":2,
    "abc":1,
}

print("=" * 50)
print("Password Analyzer Test Results")
print("=" * 50)

for password, expected_score in test_cases.items():
    result = analyze_password(password)
    actual_score = result["score"]

    assert actual_score == expected_score, (
        f"Test failed for '{password}': "
        f"expected {expected_score}, got {actual_score}"
    )

    print(
        f"PASS: {password!r} "
        f"-> score {actual_score}/{expected_score}"
    )


print("\nAll password analyzer tests passed successfully.")