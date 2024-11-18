import unittest
from Book import Book


class TestBook(unittest.TestCase):
    
    def test_book_creation(self):
        book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
        self.assertIsInstance(book_1, Book)
        
        test_title = input("Enter test book title: ")
        test_author = input("Enter test book author: ")
        test_isbn = input("Enter test book isbn: ")
        test_available = True
        
        test_book = Book(test_title, test_author, test_isbn, test_available)
        self.assertIsInstance(test_book, Book)

   
    def test_available(self):
        book_2 = Book("1984", "George Orwell", "13571357", True)

        self.assertEqual(book_2.available, True)
        book_2.borrow_book()
        result = book_2.available
        self.assertEqual(result, False)
    

if __name__ == '__main__':
    unittest.main()

