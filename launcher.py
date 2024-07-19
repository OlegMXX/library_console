from library_console.service.utils import print_all

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
            print("Library add")
        if command == "delete":
            print("Library delete")
        if command == "search":
            print("Library search")
        if command == "help":
            print("Library help")
        if command == "change_status":
            print("Library change status")
        else:
            print("Unknown command")


def main():
    print("Welcome to Library Management System.\nType in 'Help' to pull up a list of all the available commands.")

    user_interface()



if __name__ == '__main__':
    main()