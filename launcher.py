from library_console.service.utils import print_all, post_book, delete_book, change_status, search_book


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
            print("Library help")

        else:
            print("Unknown command")


def main():
    print("Welcome to Library Management System.\nType in 'help' to pull up a list of all the available commands.")

    user_interface()



if __name__ == '__main__':
    main()