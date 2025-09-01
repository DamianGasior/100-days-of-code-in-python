# 📝 Task

# Create a class Book which : 
# EAch book will have  title, author , year ; attributes will be saved in intitialization method

# Class has a 'class attribut' :  library (list of all books in the library).
# Instance method  get_info():
# Returns :
# "Title: ..., Author: ..., Year: ..."
# Create classmethod add_book_from_string(cls, text):
# Acceepts text in format  "Title;Author;Year".intitialization method
# New object Books is created and added to the library 
# Additinal as optional:
# Write  @classmethod show_library(cls), which will show all books in the library 
import logging

logging.basicConfig(
    level=logging.WARNING
)  # to see following lines with logging.debug change to: logging.basicConfig(level=logging.DEBUG), to remove logs set to: logging.basicConfig(level=logging.WARNING)


class Book:

    library=[] #lista of objects
 

    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
        Book.add_to_library(self) #IF you do this here, each book will be added to the library __init__ – obejct does exist = is in the library.
    
    
    
    def get_info(self):
        new_set=f'Title: {self.title}, Author: {self.author}, Year: {self.year}'
        return new_set

    @classmethod
    # 
    def add_book_from_string(cls,text):
        title,author,year=text.split(',')
        book1=cls(title,author,year) #call to class Book, so that a new instance class can be created with 3 arguments
        return book1.get_info()
    
    @classmethod
    def add_to_library(cls,book):
        cls.library.append(book)
        logging.debug(cls.library)
 

    @classmethod
    def show_library(cls):
        print('The library consists of :')      
        for book in cls.library:
            yield book.get_info()
         
            



b1=Book('ABC','Kowalski','1990')
print(repr(b1))
print(b1.get_info())

print(Book.add_book_from_string('CDE,Nowakowski,1880'))



for info in Book.show_library():
    print(info)