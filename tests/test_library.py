import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from service.variables import AVAILABLE, IS_GIVEN, DELETED
from errors.errors import BookDoesntExistError
from data.book import Book
from data.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(11, "Book_1", "pattern", 1990, AVAILABLE)
        self.book2 = Book(12, "Book_2", "pattern", 1990, AVAILABLE)
        self.book3 = Book(13, "Book_3", "Author1", 1990, AVAILABLE)
        self.book4 = Book(14, "Book_4", "pattern", 1990, DELETED)

        self.library_2 = Library([self.book1, self.book2])
        self.library_3 = Library([self.book1, self.book2, self.book3])
        self.library_4 = Library([self.book1, self.book2, self.book3, self.book4])

    def test_get_books(self):
        self.assertEqual(self.library_3.get_books(), [self.book1, self.book2, self.book3])

    def test_get_last_id(self):
        self.assertEqual(self.library_3.get_last_id(), 13)

    def test_add_book(self):
        self.library_2.add_book(self.book3)
        self.assertEqual(self.library_2.get_books(), self.library_3.get_books())

    def test_get_book_ind(self):
        self.assertEqual(self.library_3.get_book_ind(12), 1)

    def test_delete_book(self):
        self.library_3.delete_book(12)
        books = self.library_3.get_books(all_books=True)
        self.assertEqual(books[1].status, DELETED)
        self.assertRaises(BookDoesntExistError, self.library_3.delete_book, 12)

    def test_change_status(self):
        self.library_3.change_status(12)
        books = self.library_3.get_books(all_books=True)
        self.assertEqual(books[1].status, IS_GIVEN)

    def test_search_book(self):
        selected = [book.id for book in self.library_4.search_book("pattern")]
        self.assertEqual(selected, [11, 12])




