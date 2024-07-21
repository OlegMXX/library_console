# Класс для хранения и манипуляции данными с книгами
from datetime import datetime

from service.variables import DB_PATH, AVAILABLE, IS_GIVEN, DELETED
from errors.errors import IncorrectYearError


class Book:
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = self._validate_year(year)
        self.status = status

    # перегрузка методов для поиска максимального ID - нужно для поиска максимального
    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    @staticmethod
    def _validate_year(year):
        """
        Внутренняя функция для валидации введенного пользователем года издания книги
        Принимает параметр year при инициализации экземпляра класса и выкидывает ошибки, если что-то не так.
        Возвращает int
        """
        try:
            year = int(year)
            # в мире нет книг, изданных ранее 1377 года.
            if year < 1377 or year > datetime.now().year:
                raise IncorrectYearError
        except ValueError:
            raise IncorrectYearError

        return year

    def change_status(self):
        """Функция смены атрибута status. При запуске меняет статус на один из двух (AVIALABLE/IS_GIVEN)"""
        if self.status == AVAILABLE:
            self.status = IS_GIVEN
        else:
            self.status = AVAILABLE

    def mark_as_deleted(self):
        """Функция смены атрибута status. Помечает книгу как удаленную (DELETED)"""
        self.status = DELETED
