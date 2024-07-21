import re
from service.variables import DELETED
from errors.errors import BookDoesntExistError

class Library:
    def __init__(self, books):
        self.books = books

    def get_books(self, all_books=False):
        """
        Функция возвращает свой атрибут books в виде списка объектов Books, не отображая удаленные
        """
        if all_books:
            res = self.books
        else:
            res = [book for book in self.books if book.status != DELETED]

        return res

    def get_last_id(self):
        """
        Функция находит максимальный атрибут id в объектах Book в атрибуте books и возвращает его.
        Можно было по длине списка + 1, но надо же показать перегрузку методов класса Book.
        """
        try:
            max_id = max(self.books).id
        except ValueError:
            max_id = 0
        return max_id


    def add_book(self, book):
        """
        Функция добавляет объект Book в свой атрибут books и возвращает объект Library (сам себя с новым списком)
        """
        self.books.append(book)
        return self

    def get_book_ind(self, book_id):
        res = None
        for ind, book in enumerate(self.books):
            if book.id == book_id:
                res = ind
        return res

    def delete_book(self, book_id):
        if book_id in self.get_list_of_ids():
            self.books[self.get_book_ind(book_id)].mark_as_deleted()
            return self
        else:
            raise BookDoesntExistError

    def change_status(self, book_id):
        self.books[self.get_book_ind(book_id)].change_status()
        return self

    def search_book(self, pattern):
        selected = []
        for book in self.books:
            if (re.search(pattern.lower(), book.title.lower()) or
                    re.search(pattern.lower(), book.author.lower()) or
                    re.search(pattern, book.year)):
                selected.append(book)
        return selected

    def get_list_of_ids(self):
        return [book.id for book in self.books if book.status != DELETED]
