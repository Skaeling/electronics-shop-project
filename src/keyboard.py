from src.item import Item


class Language:
    """Класс-миксин для хранения и изменения языка раскладки клавиатуры"""
    __language = "EN"

    def __init__(self):
        pass

    @property
    def language(self):
        return self.__language

    @classmethod
    def change_lang(cls):
        """Меняет язык с английского на русский или обратно, возвращает экземпляр класса"""
        if cls.__language == "EN":
            cls.__language = "RU"
            return cls
        elif cls.__language == "RU":
            cls.__language = "EN"
            return cls


class Keyboard(Item, Language):
    def __init__(self, name, price, quantity, language=None):
        super().__init__(name, price, quantity)
        self.__language = language
