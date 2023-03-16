import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture()
def item1():
    return Item("Планшет", 25000, 5)


def test_repr(item1):
    assert repr(item1) == "Item('Планшет', 25000, 5)"


def test_str(item1):
    assert str(item1)[2] == 'а'


def test_item_from_csv():
    Item.instantiate_from_csv(path="../src/items.csv")
    assert Item.all.pop()["name"] == 'Клавиатура'


def test_item_string_to_number():
    assert Item.string_to_number('word') == None


def test_item_init(item1):
    assert item1.name == "Планшет"
    assert item1.price == 25000
    assert item1.quantity == 5


def test_item_total_price(item1):
    assert item1.calculate_total_price() == 125000


def test_item_discount(item1):
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 12500
