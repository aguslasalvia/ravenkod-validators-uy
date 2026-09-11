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
    if not isinstance(plate, str):
        raise ValueError("Invalid numberplate")

    formatted_plate = plate.replace(" ", "").upper()

    if len(formatted_plate) != 7:
        raise ValueError("Invalid numberplate")

    letters = formatted_plate[:3]
    numbers = formatted_plate[3:]

    return letters, numbers


def validate_numberplate(plate: str) -> bool:
    try:
        letters, numbers = get_formatted_plate(plate)
    except ValueError:
        return False

    return letters.isalpha() and numbers.isdigit()


def get_department_by_numberplate(plate: str) -> str:
    letters, _ = get_formatted_plate(plate)
    identifier = letters[0]
    return (
        DEPARTMENT_BY_LETTER[identifier]
        if identifier in DEPARTMENT_BY_LETTER
        else "Unknown Deparment"
    )
