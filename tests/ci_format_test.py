from ravenkod_validators_uy import format, validate


def test_ci_success_format():
    ci = "12345672"
    assert validate(ci)
    assert format(ci) == "1.234.567-2"


def test_ci_invalid_format():
    ci = "12345677"
    assert not validate(ci)
