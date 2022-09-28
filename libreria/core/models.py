from ast import AugStore
from django.db import models

# Create your models here.


class Book:
    def __init__(self, isbn, title, year, autor) -> None:
        self.isbn = isbn
        self.title = title
        self.year = year
        self.autor = autor


class Library:
    def __init__(self) -> None:
        b1 = Book('a001', 'The lord of the rings', 1954,"roberto")
        b2 = Book('a002', 'The analyst', 2002,"juan")

        self.book_list = [b1, b2]

    def add_book(self, book):
        if isinstance(book, Book):
            if book.isbn == '' or book.title == '' or book.year == '':
                return 'Missing book data'
            else:
                for b in self.book_list:
                    if isinstance(b, Book):
                        if b.isbn == book.isbn:
                            return 'This book is already in the library'                                
                    else:
                        return 'This is not a book'

                self.book_list.append(book)
                return 'Book added to library'
        else:
            return 'Missing book data'

    def list_books(self):
        return self.book_list

    def delete_book(self, isbn):
        for b in self.book_list:
            try:
                if isinstance(b, Book):
                    if b.isbn == isbn:
                        self.book_list.remove(b)
                        return 'Book deleted from library'
                else:
                    return 'The isbn is not in library'
            except:
                return 'An error has ocurred'
