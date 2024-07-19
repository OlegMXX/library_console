from service.variables import DB_PATH, AVAILABLE, IS_GIVEN

class Book():
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def change_status(self):
        if self.status == AVAILABLE:
            self.status = IS_GIVEN
        else:
            self.status = AVAILABLE
