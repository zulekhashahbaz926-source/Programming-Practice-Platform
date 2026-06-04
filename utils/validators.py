import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{4,25}$")


def validate_email(email: str) -> bool:
    return bool(email and EMAIL_PATTERN.match(email.strip()))


def validate_password(password: str) -> bool:
    return bool(password and len(password) >= 8)


def validate_username(username: str) -> bool:
    return bool(username and USERNAME_PATTERN.match(username.strip()))


def sanitize_text(value: str) -> str:
    return value.strip() if value else ""
