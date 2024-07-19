import json
from library_console.data.book import Book
from library_console.data.library import Library

IS_GIVEN = "выдана"
AVAILABLE = "в наличии"

db_path = 'db/library.json'



# COMMON
def get_books_from_json():
    with open(db_path) as f:
        book_list_of_dicts = json.loads(f.read())
        return book_list_of_dicts


def get_library():
    book_list_of_objects = []
    book_list_of_dicts = get_books_from_json()
    for book_dict in book_list_of_dicts:
        book_list_of_objects.append(Book(**book_dict))
    library = Library(book_list_of_objects)
    return library


# GET
def print_all():
    print("{:<6} | {:<40} | {:<20} | {:<8} | {:<10}".format('id', 'title', 'author', 'year', 'status'))
    print("-"*93)
    for book_object in get_library().get_books():
        book_dict = book_object.__dict__
        print("{:<6} | {:<40} | {:<20} | {:<8} | {:<10}".format(*book_dict.values()))


# POST
def post_book():
    id = get_library().get_last_id() + 1
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    status = AVAILABLE

    library = get_library().add_book(Book(id, title, author, year, status))

    to_json = []
    for book_object in library.get_books():
        to_json.append(book_object.__dict__)

    with open('db/library.json', 'w') as f:
        f.write(json.dumps(to_json, ensure_ascii=False))


