import unittest
from User import User
from Book import Book


class Library:
    books_list = list
    users_list = list

    def add_book():
        print('\nYou have selected the "Add book" option.')
        user_input_title = input("\nPlease enter the new book's title: ")
        user_input_author = input("\nPlease enter the new book's author: ")
        user_input_isbn = input("\nPlease enter the new book's ISBN number: ")
        new_book = Book(user_input_title, user_input_author, user_input_isbn, True)
        new_book_title = new_book.title

        books_str_list.append(new_book_title)
        print()
        print(new_book_title + " has been successfully added.")
        print("\nHere is the updated list of available books: ")
        print(books_str_list)

        books_list.append(new_book)


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



# These are the Users that are already in the Library system.

user_1 = User("Abigail", "0001", [book_5.title])
user_2 = User("Betty", "0002", [book_6.title])
user_3 = User("Christian", "0003", [book_7.title])

users_list = [user_1, user_2, user_3]

users_str_list = [user_1.__str__(), user_2.__str__(), user_3.__str__()]




class TestLibrary(unittest.TestCase):
    
    def test_library_add_book(self):

        Library.add_book()
        
        test_new_book = books_str_list[-1]
        
        self.assertIn(test_new_book, books_str_list)
    
   
if __name__ == '__main__':
    unittest.main()


