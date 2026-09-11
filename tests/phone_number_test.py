from ravenkod_validators_uy.phone import (
    get_clean_number,
    is_uruguayan_number,
    get_original_carrier,
)


def test_get_clean_number():
    assert get_clean_number("099 123 456") == "99123456"


def test_is_uruguayan_number_valid():
    assert is_uruguayan_number("099123456")


def test_is_uruguayan_number_invalid():
    assert not is_uruguayan_number("abc")


def test_get_original_carrier_antel():
    assert get_original_carrier("099123456") == "Antel"


def test_get_original_carrier_movistar():
    assert get_original_carrier("094123456") == "Movistar"


def test_get_original_carrier_claro():
    assert get_original_carrier("096123456") == "Claro"
