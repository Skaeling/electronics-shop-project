import csv


class InstantiateCSVError(Exception):
    """Возвращает пользовательское сообщение для исключения"""
    def __str__(self):
        return f'"Файл item.csv поврежден"'


class CSVcheck(InstantiateCSVError):

    def __init__(self, *args: object):
        super().__init__(args)
        self.path = None

    def open_file(self, path="../src/items.csv"):
        """Получает путь к файлу, проверяет сохранность всех данных в строках файла,
        если данные повреждены выбрасывает исключение,
        если данные целы возвращает список со значениями"""
        self.path = path
        with open(self.path, "r", newline='', encoding='windows-1251') as csvfile:
            allx = []
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if None in row:
                    raise InstantiateCSVError
                else:
                    allx.append(row)
        return allx
