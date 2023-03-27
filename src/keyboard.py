from src.item import Item


class Language:
    """Класс-миксин для хранения и изменения языка раскладки клавиатуры"""
    def __init__(self, name, price, quantity, language="EN"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Меняет язык с английского на русский или обратно, возвращает экземпляр класса"""
        if self.__language == "EN":
            self.__language = "RU"
            return self
        elif self.__language == "RU":
            self.__language = "EN"
            return self


class Keyboard(Language, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
