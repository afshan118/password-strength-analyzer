import re

password = input("Enter your password: ")

score = 0
suggestions = []

if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

if re.search(r"\d", password):
    score += 1
else:
    suggestions.append("Add at least one number.")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    suggestions.append("Add at least one special character.")

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)