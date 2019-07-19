class Reader:
    def __init__(self, name):
        self.name = name
        self.book = None

    def add_book(self, book):
        self.book = book