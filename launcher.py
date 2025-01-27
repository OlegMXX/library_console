from service.utils import print_all, post_book, delete_book, change_status, search_book


def user_interface():
    """
    Функция принимает команды и запускает соответсвующие функции.
    """
    while True:
        command = input("> ")
        if command == "quit":
            break
        if command == "list":
            print_all()
            continue
        if command == "add":
            post_book()
            continue
        if command == "delete":
            delete_book()
            continue
        if command == "change status":
            change_status()
            continue
        if command == "search":
            search_book()
            continue
        if command == "help":
            print("'quit' - quit library\n"
                  "'list' - open the catalog\n"
                  "'add' - add a book in the library\n"
                  "'delete' - delete a book from the library by id\n"
                  "'change status' - change status of a book by id\n"
                  "'search' - search a book by title, author or year\n")
        else:
            print("Unknown command")


def main():
    print("Welcome to Library Management System.\nType in 'help' to pull up a list of all the available commands.")

    user_interface()


if __name__ == '__main__':
    main()
