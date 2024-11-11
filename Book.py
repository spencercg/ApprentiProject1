class Book:
    title: str
    author: str
    isbn: str
    available: bool

    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available


Moby_Dick = Book("Moby Dick", "Herman Melville", "12341234", True)


