from ravenkod_validators_uy import validate


def test_valid_ci():
    assert validate("12345672")


def test_invalid_ci():
    assert not validate("12345677")
