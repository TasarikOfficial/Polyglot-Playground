import re
import getpass

password = getpass.getpass("Password: ")
checks = {
    "12+ characters": len(password) >= 12,
    "uppercase": bool(re.search(r"[A-Z]", password)),
    "lowercase": bool(re.search(r"[a-z]", password)),
    "number": bool(re.search(r"\d", password)),
    "symbol": bool(re.search(r"[^\w\s]", password)),
}
score = sum(checks.values())
labels = ["Very weak", "Weak", "Fair", "Strong", "Excellent"]
print("\nStrength:", labels[max(0, score - 1)])
for label, passed in checks.items():
    print(("✓" if passed else "✗"), label)
