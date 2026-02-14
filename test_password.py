import pytest

# Funktion der tjekker om et password er gyldigt
def validate_password(pw: str) -> bool:
    if len(pw) < 8 or len(pw) > 20:
        return False
    
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in "!@#$%^&*()" for c in pw)
    
    return has_digit and has_special


# Data-drevet test
@pytest.mark.parametrize("password,expected", [
    ("", False),
    ("Test123", False),
    ("Test123!", True),
    ("Password!", False),
    ("Password1", False),
    ("StrongPass1!", True),
])
def test_validate_password(password, expected):
    assert validate_password(password) == expected
