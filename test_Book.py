import unittest
import Book

# book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)


class TestCalc(unittest.TestCase):

    def test_available(self):
        result = self.borrow_book(book_1)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()