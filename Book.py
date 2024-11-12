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




'''
book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
book_2 = Book("1984", "George Orwell", "13571357", True)
book_3 = Book("Blood Meridian", "Cormac McCarthy", "45674567", True)
book_4 = Book("Catch-22", "Kurt Vonnegut", "24682468", True)


books_list = [book_1, book_2, book_3, book_4]

'''
