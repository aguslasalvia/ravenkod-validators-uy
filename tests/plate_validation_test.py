from ravenkod_validators_uy import validate_numberplate


def test_validate_numberpalte_successfull():
    """A plate with 3 letters and 4 digits (with a separating space) is valid."""
    plate = "ABC 1121"
    assert validate_numberplate(plate)


def test_validate_numberpalte_invalid():
    """A plate with a letter in the numeric section is invalid."""
    plate = "ABC 112A"
    assert not validate_numberplate(plate)
