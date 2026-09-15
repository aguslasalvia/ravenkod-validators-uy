def validate(ci: str) -> bool:
    """
    Validates a Uruguayan Cedula de Identidad (CI) using its check digit.

    Input: an 8-character string with 7 body digits plus 1 verification digit
    (e.g. "12345678"). Returns True if the verification digit matches the one
    computed from the body digits, False otherwise (including when the input
    is not exactly 8 characters long).
    """

    if len(ci) != 8:
        return False

    body, verified_digit = get_initial_ci_split(ci)

    digits: list = [int(char) for char in body]

    weights: list = [2, 9, 8, 7, 6, 3, 4]
    total = sum(digit * weight for digit, weight in zip(digits, weights))
    remainder = total % 10
    expected_check_digit = 0 if remainder == 0 else 10 - remainder

    return verified_digit == expected_check_digit


def format(ci: str) -> str:
    """
    Formats a Uruguayan CI, adding thousands separators and a dash before
    the check digit.

    Input: an 8-character string with no separators (e.g. "12345678").
    Output: the same CI formatted as "1.234.567-8". Does not validate the
    check digit; use `validate` first if that guarantee is needed.
    """
    body, verified_digit = get_initial_ci_split(ci)

    part1 = body[0]
    part2 = body[1:4]
    part3 = body[4:7]

    return f"{part1}.{part2}.{part3}-{verified_digit}"


def get_initial_ci_split(ci: str) -> tuple[str, int]:
    """
    Splits a raw CI string into its 7-digit body and its check digit.

    Input: an 8-character string (e.g. "12345678").
    Output: a tuple of ("1234567", 8). Does not validate length or that the
    characters are digits; callers are expected to have checked that already.
    """
    return ci[:7], int(ci[7:])
