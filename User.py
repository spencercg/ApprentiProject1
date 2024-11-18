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
        print("\nThank you for returning " + title + "!")

    def view_borrowed_books(self):
        borrowed_books = self.borrowed_books
        print(borrowed_books)
        
    def __init__(self, name, user_id, borrowed_books):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = borrowed_books




'''
user_1 = User("Abigail", "0001", [])
# user_1_name = user_1.name
user_2 = User("Betty", "0002", [])
# user_2_name = user_2.name
user_3 = User("Christian", "0003", [])
# user_3_name = user_3.name

# users_list = [user_1_name, user_2_name, user_3_name]

users_list = [user_1, user_2, user_3]
'''





