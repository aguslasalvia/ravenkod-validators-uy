from ravenkod_validators_uy import get_department_by_numberplate


def test_get_deparment_successful():
    result = get_department_by_numberplate("ABD 2018")
    assert result == "Canelones"


def test_get_deparment_invalid():
    result = get_department_by_numberplate("TAA1211")
    assert result == "Unknown Deparment"
