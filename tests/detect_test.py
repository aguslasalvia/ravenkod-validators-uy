from ravenkod_validators_uy import detect


def test_detect_ci_success():
    assert detect("12345672")


def test_detect_phone_success():
    assert detect("098123456")


def test_detect_plate_success():
    assert detect("SBA1329")


# Invalid tests
def test_detect_ci_invalid():
    assert not detect("11111119")


def test_detect_phone_invalid():
    assert not detect("01234567")


def test_detect_plate_invalid():
    assert not detect("9999991")
