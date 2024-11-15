

class Book:
    title: str
    author: str
    isbn: str
    available: bool


    def __str__(self):
        return f"{self.title}"
    

    def borrow_book(self):

        self.available = False
#            print(Book.available)
#            print(Book.title + "is available: " + Book.available)

    def return_book(self):
#        return_request = input("Please enter the title of the book you are returning: ")
        self.available = True
        print()
        print(self.title + " has been successfully returned.")
        
        
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

# books_list = [book_1.__str__(), book_2.__str__(), book_3.__str__(), book_4.__str__()]

books_list = [book_1, book_2, book_3, book_4]
'''




