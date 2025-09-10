# Task: Online Bookstore 📚
# Requirements:
# Create a class Book, which has:
# - title – the title of the book,
# - author – the author,
# - price – the price,
# - is_sold – boolean flag (default False), indicating if the book is sold.

# Add a __str__ method, which returns:
# "❌ Sold: 'Dune' - Frank Herbert (39.99 PLN)"
# "✅ Available: '1984' - George Orwell (29.99 PLN)"

# Create a class Bookstore, which has:
# - an internal list of books (books),
# - add_book(book) – adds a book to the store,
# - sell_book(title) – marks the book as sold (if available),
# - return_book(title) – marks the book as available again,
# - show_books() – displays all books in a readable way,
# - search_for_book(keyword) – returns books whose title or author contains the keyword.

# Edge cases:
# - If you try to sell a book that doesn’t exist → ValueError("This book is not in the store"),
# - If the book is already sold → ValueError("This book is already sold").

# 👉 This exercise combines everything:
# - __init__ constructor,
# - instance attributes,
# - instance methods,
# - validation,
# - __str__,
# - searching objects in a list.




class MultipleResultsError(Exception):
    """Raised when more than one result is found, but only one is expected."""
    

class Book:
    def __init__(self, title, author, price, is_sold=False):
        self.title = title
        self.author = author
        self.price = price
        self.is_sold = is_sold

    def __str__(self):
        if not self.is_sold:  # checking if the flag is set to True
            status = "Available"
            return f"{status} : {self.title} - {self.author} ({self.price})"
        elif self.is_sold:  # checking if the flag is set to False
            status = "Sold"
            return f"{status} : {self.title} - {self.author} ({self.price})"


class Bookstore:

    def __init__(self):
        self.list_of_books = []

    def add_book(self, book):
        self.list_of_books.append(book)
  

    def search_for_book_instance(self,book):
        
            book_request = next((b for b in self.list_of_books if b == book), None)
            if book_request is None:
                return None
            else:
                return book_request
      

    def search_within_a_list_of_book_objects(self,book):

        matched_books=[]
        for  b in self.list_of_books:
            if (book.lower() in   b.title.lower())  or (book.lower() in b.author.lower()):
                matched_books.append(b)
        return matched_books
                     
    

    def search_for_book(self, book):
       
            if isinstance(book, Book):#
                return self.search_for_book_instance(book)#
            else:        #tu do poprawy  
                matched_books=self.search_within_a_list_of_book_objects(book)
                yield from matched_books

    
    def search_for_book__multiple(self, book):
    
        if isinstance(book, Book):#
            return self.search_for_book_instance(book)#
        else:       
            matched_books=self.search_within_a_list_of_book_objects(book)
            return matched_books

    

    def raise_exception(self,book_to_be_sold):
                        
            titles = ', '.join([b.title for b in book_to_be_sold])#using list comprehension
            auhtors= ', '.join([ b.author for b in book_to_be_sold])
            raise MultipleResultsError (
                f'there were multiple  books found with titles and authors  {titles} and auhtors {auhtors}'
                )



    def sell_book(self, book):

        book_to_be_sold = self.search_for_book__multiple(book)
        if  isinstance(book_to_be_sold,list) and len(book_to_be_sold)>1:
            self.raise_exception(book_to_be_sold)
            
                   
        elif isinstance(book_to_be_sold,Book):
            if book_to_be_sold.is_sold is False:
                book_to_be_sold.is_sold = True
                print(
                    f"\nBook was just sold - Title : {book_to_be_sold.title}, author : {book_to_be_sold.author}"
                    )
                    # print(f'Book was just sold,{book_to_be_sold.title},{book_to_be_sold.author},{book_to_be_sold.is_sold}')
            elif book_to_be_sold and book_to_be_sold.is_sold is True:
                raise ValueError("This book is already sold")
            elif book_to_be_sold is None:
                raise ValueError("This book is not in the store")
        
        elif isinstance(book_to_be_sold,list) and len(book_to_be_sold)==1: # coulb be simple esle but leaving is , so that I can follow up in the logic in the future
            for single_position in book_to_be_sold:
            #  for b in book_to_be_sold:
                if single_position.is_sold is False:
                    single_position.is_sold = True
                    print(
                        f"\nBook was just sold - Title : {single_position.title}, author : {single_position.author}"
                    )
                    # print(f'Book was just sold,{book_to_be_sold.title},{book_to_be_sold.author},{book_to_be_sold.is_sold}')
                elif single_position and single_position.is_sold is True:
                    raise ValueError("This book is already sold")
                elif single_position is None:
                    raise ValueError("This book is not in the store")
                

    def return_book(self, book):
        book_to_be_returned = self.search_for_book__multiple(book)
        if  isinstance(book_to_be_returned,list) and len(book_to_be_returned)>1:
            self.raise_exception(book_to_be_returned)

        elif isinstance(book_to_be_returned,Book):
            if book_to_be_returned and book_to_be_returned.is_sold is True:
                book_to_be_returned.is_sold = False
                print(
                    f"\nBook was just returned - Title : {book_to_be_returned.title}, author : {book_to_be_returned.author}"
                )
            elif book_to_be_returned and book_to_be_returned.is_sold is False:
                raise ValueError("This book is not sold yet")
            elif book_to_be_returned is None:
                raise ValueError("This book is not in the store")



        elif isinstance(book_to_be_returned,list) and len(book_to_be_returned)==1:
            for single_position in book_to_be_returned:
                if single_position and single_position.is_sold is True:
                    single_position.is_sold = False
                    print(
                        f"\nBook was just returned - Title : {single_position.title}, author : {single_position.author}"
                    )
                elif single_position and single_position.is_sold is False:
                    raise ValueError("This book is not sold yet")
                elif single_position is None:
                    raise ValueError("This book is not in the store")

    def show_books(self):
        print("\nList of books with current status:")
        for book in self.list_of_books:
            print(book)
        print("End of list")


bookstore_first = Bookstore()

b1 = Book("1984", "George Orwell", "29.99 PLN")

b2 = Book("Dune", "Frank Herbert", "39.99 PLN")

b2a = Book("Dune 2", "Frank Herbert", "39.99 PLN")

b3 = Book("Lord of the Rings", "Tolkien", "49.99 PLN")

b3a = Book("Lord of the Rings 2", "Tolkien", "49.99 PLN")

b4 = Book("Harry Potter part 1", "J.K Rowling", "59.99 PLN")

b5 = Book("Harry Potter part 2 ", "J.K Rowling", "59.99 PLN")


bookstore_first.add_book(b1)
bookstore_first.add_book(b2)
bookstore_first.add_book(b2a)
bookstore_first.add_book(b3)
bookstore_first.add_book(b3a)
bookstore_first.add_book(b4)
bookstore_first.add_book(b5)

for i in bookstore_first.search_for_book("harry"):
    print(i)

bookstore_first.show_books()

bookstore_first.sell_book("1984")

bookstore_first.show_books()
# # bookstore_first.sell_book("Harry Potter") # an exceptino will be raised,as expected 


# bookstore_first.sell_book(b2)

# bookstore_first.return_book(b2)

# bookstore_first.return_book("1984")

# for i in bookstore_first.search_for_book("orwell"):
#     print(i)