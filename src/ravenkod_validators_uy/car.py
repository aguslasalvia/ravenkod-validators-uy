DEPARTMENT_BY_LETTER = {
    "A": "Canelones",
    "B": "Maldonado",
    "C": "Rocha",
    "D": "Treinta y Tres",
    "E": "Cerro Largo",
    "F": "Rivera",
    "G": "Artigas",
    "H": "Salto",
    "I": "Paysandú",
    "J": "Río Negro",
    "K": "Soriano",
    "L": "Colonia",
    "M": "San José",
    "N": "Flores",
    "O": "Florida",
    "P": "Lavalleja",
    "Q": "Durazno",
    "R": "Tacuarembó",
    "S": "Montevideo",
}


def get_formatted_plate(plate: str) -> tuple:
    """
    Normalizes a Uruguayan numberplate and splits it into letters and numbers.

    Accepts strings with or without spaces (e.g. "ABC 1234", "abc1234").
    Returns a tuple of (letters, numbers) uppercased, e.g. ("ABC", "1234").
    Raises ValueError if the input isn't a string or isn't exactly 7
    characters once spaces are removed.
    """
    if not isinstance(plate, str):
        raise ValueError("Invalid numberplate")

    formatted_plate = plate.replace(" ", "").upper()

    if len(formatted_plate) != 7:
        raise ValueError("Invalid numberplate")

    letters = formatted_plate[:3]
    numbers = formatted_plate[3:]

    return letters, numbers


def validate_numberplate(plate: str) -> bool:
    """
    Validates that a string is a well-formed Uruguayan numberplate:
    3 letters followed by 4 digits (spaces allowed and case-insensitive).

    Returns False instead of raising if the input isn't a string, has
    the wrong length, or mixes letters and digits in the wrong positions.
    """
    try:
        letters, numbers = get_formatted_plate(plate)
    except ValueError:
        return False

    return letters.isalpha() and numbers.isdigit()


def get_department_by_numberplate(plate: str) -> str:
    """
    Looks up the Uruguayan department associated with a numberplate's
    first letter.

    Input: a numberplate string (e.g. "ABC1234"). Returns the department
    name, or "Unknown Deparment" if the first letter has no mapping.
    Does not validate the full plate format; it only inspects the first
    letter, so malformed input may still raise via `get_formatted_plate`.
    """
    letters, _ = get_formatted_plate(plate)
    identifier = letters[0]
    return (
        DEPARTMENT_BY_LETTER[identifier]
        if identifier in DEPARTMENT_BY_LETTER
        else "Unknown Deparment"
    )
