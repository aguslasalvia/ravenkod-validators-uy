from ravenkod_validators_uy import validate_numberplate


def test_validate_numberpalte_successfull():
    plate = "ABC 1121"
    assert validate_numberplate(plate)


def test_validate_numberpalte_invalid():
    plate = "ABC 112A"
    assert not validate_numberplate(plate)
