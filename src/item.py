import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        """Возвращает инфо об экземпляре в формате: Item('Смартфон', 10000, 20)"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Складывать можно только экземпляров классов Phone и Item")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """Проверяет, что длина наименования товара не больше 10 символов"""
        if len(value) < 20:
            self.__name = value
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, path="../src/items.csv"):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        with open(path, "r", newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                cls.all.append(row)

    @staticmethod
    def string_to_number(number: str):
        """Статический метод, возвращающий число из числа-строки"""
        for n in number:
            if n.isdigit():
                return int(n)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
