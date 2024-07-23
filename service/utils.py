# Ключевые функции приложения, запускающие создание, удаление и манипуляцию объектами,
# выводят результаты операций в консоль

import json
from data.book import Book
from data.library import Library
from service.variables import DB_PATH, AVAILABLE, IS_GIVEN, DELETED
from errors.errors import BookDoesntExistError, IncorrectYearError


# COMMON

def init_db():
    """Зоздает json файл по заданному пути, помещая в него пустой список"""
    to_json = []
    with open(DB_PATH, 'w', encoding='utf8') as f:
        f.write(json.dumps(to_json, ensure_ascii=False))


def get_books_from_json():
    """
    Читает json файл по заданному пути, возвращает список словарей из файла.
    В случае отсутствия файла, запускает функцию его создания.
    """
    try:
        with open(DB_PATH) as f:
            book_list_of_dicts = json.loads(f.read())
            return book_list_of_dicts
    except FileNotFoundError:
        init_db()


def get_library():
    """
    Создает и возвращает объект класса Library с заполненным атрибутом books (объекты создаются из данных в json).
    Если json был пуст или не существовал, возвращает объект класса Library с маркерным атрибутом books.

    Использование функции не предполагает сохранение данных маркерного объекта Book в json ни при каких обстоятельствах.
    """
    book_list_of_objects = []
    try:
        book_list_of_dicts = get_books_from_json()
        for book_dict in book_list_of_dicts:
            book_list_of_objects.append(Book(**book_dict))
        library = Library(book_list_of_objects)
    except TypeError:
        library = Library([Book(0, "-", "-", 1988, DELETED)])
    finally:
        return library


def rewrite_json(library):
    """
    Функция перезаписи данных текущего состояния объекта Library в json
    """
    to_json = []
    for book_object in library.get_books(all_books=True):
        to_json.append(book_object.__dict__)

    with open(DB_PATH, 'w', encoding='utf8') as f:
        f.write(json.dumps(to_json, ensure_ascii=False))


def print_all():
    """Создает список объектов класса Book, передает его на функцию вывода"""
    selected = get_library().get_books()
    print_selected(selected)


# GET
def print_selected(selected):
    """Функция вывода в консоль атрибутов объектов класса Book из переданного списка"""
    print("{:<6} | {:<50} | {:<35} | {:<8} | {:<10}".format('id', 'title', 'author', 'year', 'status'))
    print("-"*140)
    for book_object in selected:
        book_dict = book_object.__dict__
        print("{:<6} | {:<50} | {:<35} | {:<8} | {:<10}".format(*book_dict.values()))


# POST
def post_book():
    """
    Функция собирающая у пользователя значения атрибутов и создающая объект класса Book.
    Добавляет этот объект в атрибут books экземпляра класса Library.
    Запускает сохранение данных из обновленного экземпляра Library в json.
    """
    id = get_library().get_last_id() + 1
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")

    status = AVAILABLE

    try:
        library = get_library().add_book(Book(id, title, author, year, status))
        to_json = []
        for book_object in library.get_books(all_books=True):
            to_json.append(book_object.__dict__)

        with open('db/library.json', 'w') as f:
            f.write(json.dumps(to_json, ensure_ascii=False))
        print("The book has been successfully added.")
    except IncorrectYearError as e:
        print(e)


# DELETE
def delete_book():
    """Принимает id экземпляра класса Book, запускает метод по маркировке книги как удаленной (DELETED)."""
    id = int(input("ID: "))
    try:
        library = get_library().delete_book(id)
        rewrite_json(library)
        print("Book has been deleted")
    except BookDoesntExistError as e:
        print(e)


# PATCH
def change_status():
    """Принимает id экземпляра класса Book, запускает метод по смене атрибута status (на AVIALABLE/IS_GIVEN)."""
    id = int(input("ID: "))
    try:
        library = get_library().change_status(id)
        rewrite_json(library)
        print("Book status has been changed")
    except BookDoesntExistError as e:
        print(e)


# SEARCH
def search_book():
    """Принимает паттерн поиска, запускает метод поиска, возвращает список объектов Book, подходящие к паттерну."""
    pattern = input("Search: ")
    selected = get_library().search_book(pattern)
    print_selected(selected)
