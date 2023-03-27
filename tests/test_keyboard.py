import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def key():
    return Keyboard('Defender', 5000, 2)


def test_init(key):
    assert key.language == "EN"


def test_change_lang(key):
    assert key.change_lang().language == "RU"
    assert key.change_lang().language == "EN"
