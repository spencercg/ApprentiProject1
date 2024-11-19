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

    def view_borrowed_books(self):
        return self.borrowed_books
        
    def __init__(self, name, user_id, borrowed_books):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = borrowed_books
