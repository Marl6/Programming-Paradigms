class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nGenre: {self.genre}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print(book)
            print()

    def search_book(self, searchby, keyword):
        found_books=[]
        if searchby.lower() == "title":
            found_books = [book for book in self.books if keyword.lower() in book.title.lower()]
        elif searchby.lower() == "author":
            found_books = [book for book in self.books if keyword.lower() in book.author.lower()]
        elif searchby.lower() == "publication_year":
            found_books = [book for book in self.books if keyword.lower() in book.publication_year.lower()]
        elif searchby.lower() == "genre":
            found_books = [book for book in self.books if keyword.lower() in book.genre.lower()]
        else:
            print("Invalid Book Criteria!")
            return
        
        if found_books:
            print("Search Results:")
            for book in found_books:
                print(book)
                print()

        else:
            print("No book found!")

# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "2024", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "2020", "Fiction")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.display_books()

library.search_book("publication_year", "2020")

