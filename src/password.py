import re

def is_valid_password(password):
    # Check length and allowed characters all at once
    pattern = re.compile(r"^[A-Za-z0-9~!@#$%&_\-+=`|\\(){}\[\]:;'<>,.?/]{12,30}$")
    if not pattern.fullmatch(password):
        return False

    # Check required character types separately
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[~!@#$%&_\-+=`|\\(){}\[\]:;'<>,.?/]", password):
        return False

    return True