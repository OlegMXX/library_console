import json


class Library:
    def __init__(self, books):
        self.books = books

    def get_books(self):
        """
        Функция возвращает свой атрибут books в виде списка объектов Books
        """
        return self.books

    def get_last_id(self):
        """
        Функция находит максимальный атрибут id в объектах Book в атрибуте books и возвращает его
        """
        max_id = max(self.books).id
        return max_id


    def add_book(self, book):
        """
        Функция добавляет объект Book в свой атрибут books и возвращает объект Library (сам себя с новым списком)
        """
        self.books.append(book)
        return self

    def get_book(self, book_id):
        res = None
        for ind, book in enumerate(self.books):
            if book.id == book_id:
                res = ind
        return res

    def delete_book(self, book_id):
        self.books.pop(self.get_book(book_id))
        return self

    def change_status(self, book_id, status):
        pass
