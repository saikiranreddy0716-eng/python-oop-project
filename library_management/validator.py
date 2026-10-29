"""Reusable validation helpers."""
from .exceptions import ValidationError


def required_text(value: str, field_name: str) -> str:
    """Return trimmed text or raise an error when it is empty."""
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{field_name} cannot be empty.")
    return value.strip()


def positive_int(value: int, field_name: str) -> int:
    """Validate that a value is a positive integer (not a boolean)."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValidationError(f"{field_name} must be a positive whole number.")
    return value


def non_negative_int(value: int, field_name: str) -> int:
    """Validate that a value is a non-negative integer."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValidationError(f"{field_name} must be zero or a positive whole number.")
    return value


def valid_email(value: str) -> str:
    """Perform a basic email-format check and return the trimmed email."""
    email = required_text(value, "Email")
    if "@" not in email or "." not in email.split("@")[-1] or " " in email:
        raise ValidationError("Please enter a valid email address.")
    return email
