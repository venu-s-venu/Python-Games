import re
import getpass

RULES = [
    ("length", "Password length must be between 8 and 32 characters"),
    ("upper", "At least one uppercase letter (A-Z)"),
    ("lower", "At least one lowercase letter (a-z)"),
    ("digit", "At least one digit (0-9)"),
    ("special", "At least one special character from @#$%^&+="),
]

SPECIAL_CHARS = r"@#$%^&+="


def check_password(password: str):
    """
    Returns (is_valid: bool, failures: list[str], score: int)
    score is number of passed checks (0-5) plus bonus for length > 12.
    """
    failures = []

    # Length
    if not (8 <= len(password) <= 32):
        failures.append(RULES[0][1])

    # Uppercase
    if not re.search(r"[A-Z]", password):
        failures.append(RULES[1][1])

    # Lowercase
    if not re.search(r"[a-z]", password):
        failures.append(RULES[2][1])

    # Digit
    if not re.search(r"\d", password):
        failures.append(RULES[3][1])

    # Special characters (only those listed)
    if not re.search(rf"[{re.escape(SPECIAL_CHARS)}]", password):
        failures.append(RULES[4][1])

    # Calculate score: 1 point per passed rule
    passed = 5 - len(failures)
    # length bonus: +1 if strong length (>12)
    bonus = 1 if len(password) > 12 else 0
    score = passed + bonus

    is_valid = len(failures) == 0
    return is_valid, failures, score


def strength_from_score(score: int):
    """Map numeric score to strength label"""
    # score range: 0..6
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    return "Strong"


def interactive_mode():
    print("Password rules:")
    for i, (_, msg) in enumerate(RULES, 1):
        print(f"{i}. {msg}")
    print("Type 'quit' to exit without saving.\n")

    while True:
        # Use getpass to hide input; fallback to input if getpass fails
        try:
            pwd = getpass.getpass("Enter password: ").strip()
        except Exception:
            pwd = input("Enter password: ").strip()

        if pwd.lower() == "quit":
            print("Exiting. No password saved.")
            break

        is_valid, failures, score = check_password(pwd)
        strength = strength_from_score(score)

        print(f"\nStrength: {strength} (score: {score})")
        if is_valid:
            print("Password is valid. ✅")
            # If you want to accept and exit:
            break
        else:
            print("Password is invalid. Fix the following:")
            for f in failures:
                print(" -", f)
            print("\nTry again or type 'quit' to stop.\n")


if __name__ == "__main__":
    interactive_mode()
