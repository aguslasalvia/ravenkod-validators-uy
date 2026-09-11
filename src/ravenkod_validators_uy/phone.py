
ORIGINAL_CARRIER_BY_PREFIX = {
    "91": "Antel",
    "92": "Antel",
    "93": "Movistar",
    "94": "Movistar",
    "95": "Movistar",
    "96": "Claro",
    "97": "Claro",
    "98": "Antel",
    "99": "Antel",
}


def get_clean_number(phone_number: str) -> str:
    """
    Normalizes a Uruguayan mobile number to its canonical form:
    8 digits, no spaces, no +598, no optional leading 0.

    Accepts: "099 123 456", "099123456", "+59899123456", "99123456"
    Returns: "99123456"
    """
    if not isinstance(phone_number, str):
        raise ValueError("Invalid phone number")

    cleaned = phone_number.replace(" ", "").replace("-", "")

    if cleaned.startswith("+598"):
        cleaned = cleaned[4:]
    elif cleaned.startswith("598"):
        cleaned = cleaned[3:]

    if cleaned.startswith("0"):
        cleaned = cleaned[1:]

    if len(cleaned) != 8 or not cleaned.isdigit():
        raise ValueError("Invalid phone number")

    return cleaned


def is_uruguayan_number(phone_number: str) -> bool:
    """
    Validates that the number is a Uruguayan mobile number:
    8 national digits, always starting with 9.
    """
    try:
        clean = get_clean_number(phone_number)
    except ValueError:
        return False

    return clean.startswith("9")


def get_original_carrier(phone_number: str) -> str:

    if not is_uruguayan_number(phone_number):
        raise ValueError("Invalid phone number")

    clean = get_clean_number(phone_number)
    prefix = clean[:2]

    return ORIGINAL_CARRIER_BY_PREFIX.get(prefix, "Unknown")
