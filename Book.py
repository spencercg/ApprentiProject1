class Book:
    title: str
    author: str
    isbn: str
    available: bool


# I need to update borrow and return so that status of availability actually changes


    def borrow_book(self):
        borrow_request = input("Please enter the title of the book you would like to request: ")
        Book.available = False
        print(borrow_request + " has been successfully checked out.")
        print(Book.available)

    def return_book(self):
        return_request = input("Please enter the title of the book you are returning: ")
        Book.available = True
        print(return_request + " has been successfully returned")
    '''
    def create_book(self): 
        print("You have selected the Add Book option.")       
        self.title = input("Please enter the title of the new book: ")
        print(self.title)
    '''
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available





Moby_Dick = Book("Moby Dick", "Herman Melville", "12341234", True)

# Moby_Dick.borrow_book()

print(Moby_Dick.author)

