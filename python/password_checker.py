import re, getpass

password = getpass.getpass("Password: ")
checks = {
    "12+ characters": len(password) >= 12,
    "uppercase": bool(re.search(r"[A-Z]", password)),
    "lowercase": bool(re.search(r"[a-z]", password)),
    "number": bool(re.search(r"\d",", password)),
    "symbol": bool(re.search(r"[^\w\s]", password)),
}
score = sum(checks.values())
print("\nStrength:", ["Very weak", "Weak", "Fair", "Strong", "Excellent"][max(0, score - 1)])
for label, passed in checks.items():
    print(("✓" if passed else "✗"), label)
