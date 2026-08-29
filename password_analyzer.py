import re

def check_length(password):
    length = len(password)
    if length >= 16:
        return 3
    elif length >= 12:
        return 2
    elif length >= 8:
        return 1
    else:
        return 0

def check_variety(password):
    score = 0
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    return score

def analyze(password):
    common = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]
    if password.lower() in common:
        return {"score": 0, "level": "Cok Zayif", "note": "Yaygin sifre listesinde!"}

    score = check_length(password) + check_variety(password)

    if score >= 6:
        level = "Cok Guclu"
    elif score >= 4:
        level = "Guclu"
    elif score >= 2:
        level = "Orta"
    else:
        level = "Zayif"

    return {"score": score, "level": level, "note": ""}

if __name__ == "__main__":
    test_passwords = ["123456", "hello", "Merhaba1", "Merhaba123!", "xK9#mL2$vQ7@nP4"]
    for pw in test_passwords:
        result = analyze(pw)
        print(f"{pw:20} -> {result['level']} (puan: {result['score']}) {result['note']}")
