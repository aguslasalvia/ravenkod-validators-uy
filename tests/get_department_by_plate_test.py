from ravenkod_validators_uy import get_department_by_numberplate


def test_get_deparment_successful():
    """A plate whose first letter is mapped returns the matching department."""
    result = get_department_by_numberplate("ABD 2018")
    assert result == "Canelones"


def test_get_deparment_invalid():
    """A plate whose first letter has no mapping returns "Unknown Deparment"."""
    result = get_department_by_numberplate("TAA1211")
    assert result == "Unknown Deparment"
