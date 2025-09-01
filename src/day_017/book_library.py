# Task: Library System 📚
# Requirements:
# Create a class Book that has:
# - title – the title of the book,
# - author – the author of the book,
# - is_borrowed – a boolean flag (default False) indicating whether the book is borrowed.
# Add a __str__ method that returns a description of the book in the form:
# - "📕 Borrowed: 'Pan Tadeusz' - Adam Mickiewicz"
# - "📗 Available: 'Lalka' - Bolesław Prus".
# Create a class Library that has:
# - an internal list of books books,
# - a method add_book(book) – adds a book to the library,
# - a method borrow_book(title) – sets is_borrowed=True for the book with the given title (if available),
# - a method return_book(title) – sets is_borrowed=False (returns the book),
# - a method show_books() – displays all books in a readable format.
# Handle edge cases:
# - If you try to borrow a book that doesn’t exist → raise ValueError("No such book in the library"),
# - If the book is already borrowed → raise ValueError("The book is already borrowed").

# 👉 This task is very similar to the bank queue exercise –
# you also have a list of objects, operations for adding/retrieving, and validation, but in a different context.

class Book:
    def __init__(self, title,author,library, is_borrowed=False): #initializer, sets the intances attributes
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed # be default set to False, if requider can  be changed to True
        library.add_book(self)

    def __str__(self):
        if self.is_borrowed==True:
            return f'Book borrowed: {self.title} - {self.author}'
        elif self.is_borrowed==False:
            return f'Book is available: {self.title} - {self.author}'
        else:
            return f'Book is unavailable'
        

class Library:

    def __init__(self):
        self.list_of_books=[]



    def add_book(self,book):
        self.list_of_books.append(book)

    
    def borrow_book(self,title):
        book_on_shelf=next((book for book  in self.list_of_books if book.title==title),None) # in case I would need index  >> iks=next((i for i,book in enumerate(cls.list_of_books) if book.title==title),None)
        if book_on_shelf:
            book_on_shelf.is_borrowed=True
            print(f'\nBook to be borrowed : {title}\n')
            self.show_books()
        elif book_on_shelf and book_on_shelf.is_borrowed is False:
            raise ValueError ('Book is owned by the library  but currently is already borrowed')
        else:
   
            raise ValueError ('No such book in the library')    
    
    def return_book(self,title):
        book_not_in_library=next((book for book in self.list_of_books if book.title==title and book.is_borrowed is True),None)
        if book_not_in_library:
            book_not_in_library.is_borrowed=False
            print(f'\n Book is being returned: {title}\n')
            self.show_books()
        else:
            return 'Book is already available in the library'

    
    
    def show_books(self):
        for book in self.list_of_books:
            print (book)



lib=Library() # instance of class libaryr
Book('Lord of the rings','Tolkien', lib)
Book('HArryPotter','J.K Rowling',lib)

lib.show_books() 

lib.borrow_book('HArryPotter') 

lib.return_book('HArryPotter') 

