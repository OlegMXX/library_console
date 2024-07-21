class IncorrectYearError(Exception):
    """Исключение - неправильно введен год написания книги"""
    def __str__(self):
        return f'The year was typed incorrectly. It must be between 1377 and actual year'


class BookDoesntExistError(Exception):
    """Исключение - запрашиваемой по ID книги нет в библиотеке """
    def __str__(self):
        return f'The book you are trying to delete is not exist'
