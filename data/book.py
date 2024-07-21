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

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    @staticmethod
    def _validate_year(year):
        try:
            year = int(year)
            # в мире нет книг, изданных ранее 1377 года.
            if year < 1377 or year > datetime.now().year:
                raise IncorrectYearError
        except ValueError:
            raise IncorrectYearError

        return year

    def change_status(self):
        if self.status == AVAILABLE:
            self.status = IS_GIVEN
        else:
            self.status = AVAILABLE

    def mark_as_deleted(self):
        self.status = DELETED
