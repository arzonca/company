from library.exceptions import NotEnoughBooksToRentInLibrary    #sciezka do katalogu projektu pomimo tego, ze
# pliki library.py i exceptions.py sa we wspolnym podkatalogu library w katalogu company


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def rent_book(self, reader):
        not_rent_books = [book for book in self.books if not book.is_rent]
        if not not_rent_books:     #sprawdzamy czy sa ksiązki do wypozyczenia, jesli jest pusta ta lista
            raise NotEnoughBooksToRentInLibrary()   #po kliknieciu Alt + Enter
        book = not_rent_books.pop()   #usun ostatnia ksiązke z listy niewypozyczonych,. bo ja własnie wypozyczamy
        book.rent()                #wypozycz
        reader.add_book(book)             #ustaw ja uzytownikowi


    def get_book_back(self, book):
        book.get_back()

