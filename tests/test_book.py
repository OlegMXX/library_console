import sys
import os
import unittest
from datetime import datetime

sys.path.append(os.path.join(os.getcwd(), '..'))
from service.variables import AVAILABLE, IS_GIVEN, DELETED
from errors.errors import IncorrectYearError
from data.book import Book


class TestBook(unittest.TestCase):
    def test_bigger_smaller(self):
        book1 = Book(12, "Book1", "Author1", 1990, AVAILABLE)
        book2 = Book(14, "Book2", "Author2", 1990, AVAILABLE)
        self.assertTrue(book1 < book2)
        self.assertFalse(book2 < book1)

    def test_incorrect_year(self):
        self.assertRaises(IncorrectYearError, Book, 12, "Book1", "Author1", 1111, AVAILABLE)
        self.assertRaises(IncorrectYearError, Book, 12, "Book1", "Author1", datetime.now().year + 1, AVAILABLE)

    def test_change_status(self):
        book = Book(12, "Book", "Author", 1990, IS_GIVEN)
        book.change_status()
        self.assertEqual(book.status, AVAILABLE)

    def test_delete_book(self):
        book = Book(12, "Book", "Author", 1990, IS_GIVEN)
        book.mark_as_deleted()
        self.assertEqual(book.status, DELETED)