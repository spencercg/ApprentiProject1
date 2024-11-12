from Book import Book
from User import User

class Library:
    books_list = list
    users_list = list



    def __init__(self):
        self.books_list = books_list
        self.users_list = users_list



# These are the books that are already in the library.

book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
book_1_title = book_1.title

book_2 = Book("1984", "George Orwell", "13571357", True)
book_2_title = book_2.title

book_3 = Book("Blood Meridian", "Cormac McCarthy", "45674567", True)
book_3_title = book_3.title

book_4 = Book("Catch-22", "Kurt Vonnegut", "24682468", True)
book_4_title = book_4.title


books_list = [book_1_title, book_2_title, book_3_title, book_4_title]


# These are the Users that are already in the Library system.

user_1 = User("Abigail", "0001", [])
user_1_name = user_1.name
user_2 = User("Betty", "0002", [])
user_2_name = user_2.name
user_3 = User("Christian", "0003", [])
user_3_name = user_3.name

users_list = [user_1_name, user_2_name, user_3_name]




# Welcome screen for the Library Management Systemm

print("Welcome to the Library Management System. Below is a list of the available options:"
 "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
 "\n 7) List available books" )

user_input = input("Please enter the number associated with the option you would like to select: ")


if user_input == str(1):
    print('You have selected the "Add book" option.')
    user_input_title = input("Please enter the new book's title: ")
    user_input_author = input("Please enter the new book's author: ")
    user_input_isbn = input("Please enter the new book's ISBN number: ")
    new_book = Book(user_input_title, user_input_author, user_input_isbn, True)
    new_book_title = new_book.title
    books_list.append(new_book_title)
    print("Thank you!\n\nHere is the updated list of available books: ")
    print(books_list)

elif user_input == str(2):
    print('You have selected the "Remove book" option.')
    print("Below is the list of available books: ")
    print(books_list)
    bye_book_title = input("Please enter the title of the book you would like to remove: ")
    books_list.remove(bye_book_title)
    print("Below is the updated list of available books: ")
    print(books_list)

elif user_input == str(3):
    print('You have selected the "Add user" option.')
    new_user_name = input("Please enter the new user's name: ")
    users_list.append(new_user_name)
    print("User has been added. Below is the updated list of users: ")
    print(users_list)

elif user_input == str(4):
    print('You have selected the "Remove user" option.')
    print("Below is the current list of user names: ")
    print(users_list)
    bye_user_name = input("Please enter the name of the user you would like to remove: ")
    users_list.remove(bye_user_name)
    print("User has been removed. Below is the updated list of users: ")
    print(users_list)


elif user_input == str(7):
    print('You have selected the "List available books" option.')
    print('Below is the list of available books: ')
    print(books_list)

else:
    print('\nInvalid input. \n\nPlease select from the list of available options: '
    '\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book' 
    '\n 7) List available books')










