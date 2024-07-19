import json


class Library():
    def __init__(self, books):
        self.books = books

    def get_last_id(self):
        pass

    def book_list(self):
        pass

    def add_book(self, book):
        last_id = self.get_last_id()
        book.id = last_id + 1

    def get_book(self, book_id):
        pass

    def delete_book(self, book_id):
        pass

    def change_status(self, book_id, status):
        pass
