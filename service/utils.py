import json
from library_console.data.book import Book

db_path = 'db/library.json'


def get_books_from_json():
    with open(db_path) as f:
        book_list_of_dicts = json.loads(f.read())
        return book_list_of_dicts


def get_books_objects():
    book_list_of_objects = []
    book_list_of_dicts = get_books_from_json()
    for book_dict in book_list_of_dicts:
        book_list_of_objects.append(Book(**book_dict))
    return book_list_of_objects


def get_next_id():



# GET
def print_all():
    print("{:<6} | {:<40} | {:<20} | {:<8} | {:<10}".format('id', 'title', 'author', 'year', 'status'))
    print("-"*93)
    for book_object in get_books_objects():
        book_dict = book_object.__dict__
        print("{:<6} | {:<40} | {:<20} | {:<8} | {:<10}".format(*book_dict.values()))


# POST
def post_book(title, author, year, status):

