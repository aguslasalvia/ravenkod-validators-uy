from .ci import validate, format
from .car import validate_numberplate, get_department_by_numberplate
from .phone import is_uruguayan_number, get_original_carrier
from .detect import detect

__all__ = [
    "validate",
    "format",
    "validate_numberplate",
    "get_department_by_numberplate",
    "is_uruguayan_number",
    "get_original_carrier",
    "detect",
]
