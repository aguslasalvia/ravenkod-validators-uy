from .ci import validate as validate_ci
from .car import validate_numberplate
from .phone import is_uruguayan_number


def detect(value: str) -> str | None:
    """
    Guesses which kind of Uruguayan identifier a string is, by trying each
    validator in order: phone, then numberplate, then CI.

    Returns "phone", "car", or "ci" for the first matching type, or None if
    the value doesn't validate as any of them. Note the check order matters
    for ambiguous inputs that could satisfy more than one validator.
    """
    if is_uruguayan_number(value):
        return "phone"
    if validate_numberplate(value):
        return "car"
    if validate_ci(value):
        return "ci"

    return None
