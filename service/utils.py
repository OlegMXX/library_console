import json
from library_console.data.book import Book
from library_console.data.library import Library
from service.variables import DB_PATH, AVAILABLE, IS_GIVEN, DELETED
from errors.errors import BookDoesntExistError, IncorrectYearError


# COMMON

def init_db():
    to_json = []
    with open(DB_PATH, 'w') as f:
        f.write(json.dumps(to_json, ensure_ascii=False))


def get_books_from_json():
    try:
        with open(DB_PATH) as f:
            book_list_of_dicts = json.loads(f.read())
            return book_list_of_dicts
    except FileNotFoundError as e:
        init_db()




def get_library():
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
    to_json = []
    for book_object in library.get_books(all_books=True):
        to_json.append(book_object.__dict__)

    with open(DB_PATH, 'w') as f:
        f.write(json.dumps(to_json, ensure_ascii=False))


def print_all():
    selected = get_library().get_books()
    print_selected(selected)


# GET
def print_selected(selected):
    print("{:<6} | {:<50} | {:<35} | {:<8} | {:<10}".format('id', 'title', 'author', 'year', 'status'))
    print("-"*140)
    for book_object in selected:
        book_dict = book_object.__dict__
        print("{:<6} | {:<50} | {:<35} | {:<8} | {:<10}".format(*book_dict.values()))


# POST

def post_book():
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
    id = int(input("ID: "))
    try:
        library = get_library().delete_book(id)
        rewrite_json(library)
        print("Book has been deleted")
    except BookDoesntExistError as e:
        print(e)


# PATCH
def change_status():
    id = int(input("ID: "))
    library = get_library().change_status(id)
    rewrite_json(library)


# SEARCH
def search_book():
    pattern = input("Search: ")
    selected = get_library().search_book(pattern)
    print_selected(selected)
