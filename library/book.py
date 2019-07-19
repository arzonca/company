class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_rent = False

    def rent(self):
        self.is_rent = True

    def get_back(self):
        self.is_rent = False
