def validate(ci: str) -> bool:
    body, verified_digit = get_initial_ci_split(ci)

    digits: list = [int(char) for char in body]

    weights: list = [2, 9, 8, 7, 6, 3, 4]
    total = sum(digit * weight for digit, weight in zip(digits, weights))
    remainder = total % 10
    expected_check_digit = 0 if remainder == 0 else 10 - remainder

    return verified_digit == expected_check_digit


def format(ci: str) -> str:
    """
    Recieves an CI with no separations what so ever and returns a formated CI
    Input: 12345678
    Output: 1.234.567-8
    """
    body, verified_digit = get_initial_ci_split(ci)

    part1 = body[0]
    part2 = body[1:4]
    part3 = body[4:7]

    return f"{part1}.{part2}.{part3}-{verified_digit}"


def get_initial_ci_split(ci: str) -> tuple[str, int]:
    return ci[:7], int(ci[7:])
