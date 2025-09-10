import pytest
import online_bookstore

# 1. from online_bookstore import Book, Bookstore, MultipleResultsError
# You import specific classes/exceptions.
# Then you can use them without a prefix:
# book = Book("1984", "George Orwell", "29.99 PLN")


# This is shorter and more readable if you are testing these specific classes.
# 2. import online_bookstore
# You import the entire module.
# Then you must use the prefix:
# book = online_bookstore.Book("1984", "George Orwell", "29.99 PLN")
# bs = online_bookstore.Bookstore()


# This is more explicit (you can immediately see that Book comes from online_bookstore).
# It takes a bit longer to write, but in large projects it is sometimes preferred
# because it reduces the risk of name collisions.


# 🔹 1. Book class

# ✅ Test initialization (title, author, price, is_sold defaults to False).
# ✅ Test __str__ method for available and sold books.

@pytest.fixture

def bookstore():
    bs=online_bookstore.Bookstore()
    b1=online_bookstore.Book("1984", "George Orwell", "29.99 PLN")
    b2=online_bookstore.Book("Dune", "Frank Herbert", "39.99 PLN")
    b3=online_bookstore.Book("Harry Potter", "J.K Rowling", "59.99 PLN")
    b4=online_bookstore.Book("Harry Potter part 2 ", "J.K Rowling", "59.99 PLN")
    bs.add_book(b1)
    bs.add_book(b2)
    bs.add_book(b3)
    bs.add_book(b4)

    return bs


def test_add_book(bookstore):
    assert len(bookstore.list_of_books)==4
    assert isinstance(bookstore.list_of_books[0],online_bookstore.Book)
    assert bookstore.list_of_books[0].title=="1984"

def test_search_for_book(bookstore):
    harry_book=bookstore.list_of_books[2]
    
    assert isinstance(harry_book,online_bookstore.Book)
    # assert len(harrys_book)==1
    assert str(harry_book)=='Available : Harry Potter - J.K Rowling (59.99 PLN)'
    
    books=list(bookstore.search_for_book("harry"))
    assert str(books[0])=='Available : Harry Potter - J.K Rowling (59.99 PLN)'
    assert str(books[1])=='Available : Harry Potter part 2  - J.K Rowling (59.99 PLN)'

def test_sell_book(bookstore):
    sold_book=bookstore.list_of_books[0]
    bookstore.sell_book(sold_book)
    assert sold_book.is_sold==True
    assert str(sold_book)=='Sold : 1984 - George Orwell (29.99 PLN)'


    bookstore.sell_book("dune")
    second_book_sold=list(bookstore.search_for_book("dune"))
    assert str(second_book_sold[0])=='Sold : Dune - Frank Herbert (39.99 PLN)'
    assert second_book_sold[0].is_sold==True

    with pytest.raises(ValueError):
        bookstore.sell_book("dune")
        bookstore.sell_book(sold_book)





def test_return_book(bookstore):
    sold_book=bookstore.list_of_books[0]
    bookstore.sell_book(sold_book)
    assert sold_book.is_sold==True
    assert str(sold_book)=='Sold : 1984 - George Orwell (29.99 PLN)'


    returned_book=bookstore.return_book("1984")
    returned_book=bookstore.list_of_books[0]
    assert returned_book.is_sold==False



def test_raise_exception(bookstore):
       
    with pytest.raises(online_bookstore.MultipleResultsError):
        bookstore.sell_book("har")



