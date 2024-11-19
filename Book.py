
class Book:
    title: str
    author: str
    isbn: str
    available: bool


    def __str__(self):
        return f"{self.title}"
    

    def borrow_book(self):

        self.available = False


    def return_book(self):
        self.available = True
        print()
        print(self.title + " is now available to be borrowed.")
        
        
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

