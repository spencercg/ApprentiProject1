import unittest
from Book import Book




class TestCalc(unittest.TestCase):

    def test_available(self):
        book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
        self.assertEqual(book_1.available, False)
        book_1.borrow_book()
        result = book_1.available
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()