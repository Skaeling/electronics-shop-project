import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def key():
    return Keyboard('Defender', 5000, 2)


def test_init(key):
    assert key.language == "EN"


def test_change_lang(key):
    key.change_lang()
    assert str(key.language) == "RU"
    key.change_lang()
    assert str(key.language) == "EN"
