import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone('Huawei', 32000, 5, 1)


def test_init_phone(phone):
    assert phone.number_of_sim == 1


def test_repr(phone):
    assert repr(phone) == "Phone('Huawei', 32000, 5, 1)"


def test_number_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 4.5
