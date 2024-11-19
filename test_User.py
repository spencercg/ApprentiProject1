import unittest
from User import User
from Book import Book


class TestUser(unittest.TestCase):
    
    def test_user_borrowing(self):
        book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
        user_1 = User("Abigail", "0001", [])
        
        user_1.borrow_book(book_1)
        self.assertIn(book_1, user_1.borrowed_books)


    def test_user_returning(self):
        book_2 = Book("1984", "George Orwell", "13571357", False)
        user_2 = User("Betty", "0002", [book_2.title])

        user_2.return_book(book_2.title)
        self.assertNotIn(book_2.title, user_2.borrowed_books)

    def test_user_view_books(self):
        book_2 = Book("1984", "George Orwell", "13571357", False)
        user_2 = User("Betty", "0002", [book_2.title])

        test_borrowed_book_list = user_2.view_borrowed_books()
        self.assertIn(book_2.title, test_borrowed_book_list)


if __name__ == '__main__':
    unittest.main()