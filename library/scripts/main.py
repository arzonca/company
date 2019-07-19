from library.book import Book
from library.library import Library
from library.reader import Reader

if __name__ == '__main__':
    books = [Book("Harry potter", "J.K.Rowling"), Book("Lotr", "Tolkien")]
    reader1 = Reader("Piotr")
    library = Library()

    library.add_book(books[0])
    library.add_book(books[1])
