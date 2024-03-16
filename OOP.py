# We created a book class wherein we initialize its characteristics of title, author, publication_year, and genre
class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nGenre: {self.genre}"

# We then created a library class where we instantiate the characteristics of a library (which is given in the instructions)
class Library:
    def __init__(self):
        self.books = []
        
    # this function simply adds book in the self.books array
    def add_book(self, book):
        self.books.append(book)

    #this function simply shows/prints the books in the library
    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print(book)
            print()

    # this function simply search for a specific book in the library using a specific keywords or unique characteristics of a book
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

# what we do here is that we created an object by specifying the characteristics of the book
book1 = Book("Rich Dad Poor Dad", "F. Scott Fitzgerald", "2024", "Fiction")
book2 = Book("A Subtle Art of Not Giving a F*ck", "Harper Lee", "2020", "Fiction")

# sample usage of adding the object book into our library
library = Library()
library.add_book(book1)
library.add_book(book2)

# sample usage of displaying the list of books
library.display_books()

# sample usage of searching a specific book in the library
library.search_book("publication_year", "2020")

