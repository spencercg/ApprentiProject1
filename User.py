from Book import Book

class User:
    name: str
    user_id: str
    borrowed_books: list

    def __str__(self):
        return f"{self.name}"

    def borrow_book(self, title):
        borrowed_books = self.borrowed_books
        borrowed_books.append(title)
        
        
    def return_book(self, title):
        borrowed_books = self.borrowed_books
        borrowed_books.remove(title)
        # print("\nThank you for returning " + title + "!")

    def view_borrowed_books(self):
        # borrowed_books = self.borrowed_books
        return self.borrowed_books
        
    def __init__(self, name, user_id, borrowed_books):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = borrowed_books



'''
# These are the books that are in the library and available to be checked out.

book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
book_2 = Book("1984", "George Orwell", "13571357", True)
book_3 = Book("Blood Meridian", "Cormac McCarthy", "45674567", True)
book_4 = Book("Catch-22", "Kurt Vonnegut", "24682468", True)


books_str_list = [book_1.__str__(), book_2.__str__(), book_3.__str__(), book_4.__str__()]

books_list = [book_1, book_2, book_3, book_4]


# These are the books that are currently checked out.

book_5 = Book("Brave New World", "Aldous Huxley", "23452345", False)

book_6 = Book("The Divine Invasion", "Philip K. Dick", "34563456", False)

book_7 = Book("The Magic Mountain", "Thomas Mann", "56785678", False)

checked_out_master_list = [book_5, book_6, book_7]




user_1 = User("Abigail", "0001", [book_5.title])
user_2 = User("Betty", "0002", [book_6.title])
user_3 = User("Christian", "0003", [book_7.title])

users_list = [user_1, user_2, user_3]

users_str_list = [user_1.__str__(), user_2.__str__(), user_3.__str__()]

'''

