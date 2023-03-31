import pytest
from src.item import Item
from src.instantiate_csv_error import InstantiateCSVError


@pytest.fixture()
def item1():
    return Item("Планшет", 25000, 5)


@pytest.fixture()
def item2():
    return Item("Ноутбук", 35000, 4)


def test_repr(item1):
    assert repr(item1) == "Item('Планшет', 25000, 5)"


def test_str(item1):
    assert str(item1)[2] == 'а'


def test_item_from_csv():
    Item.instantiate_from_csv(path="../src/items2.csv")  # неповрежденный файл
    assert Item.all.pop()["name"] == 'Клавиатура'

    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):  # поврежденный файл
        Item.instantiate_from_csv(path="../src/items.csv")

    with pytest.raises(FileNotFoundError):  # нет такого файла
        Item.instantiate_from_csv(path="../src/BADWAY.csv")


def test_item_string_to_number():
    assert Item.string_to_number('word') is None
    assert Item.string_to_number('5') == 5


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


def test_item_add(item1, item2):
    with pytest.raises(ValueError):
        assert item1 + 3
    assert item1 + item2 == 9
