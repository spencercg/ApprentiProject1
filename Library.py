class Library:
    books_list = list
    users_list = list



    



    def __init__(self):
        self.books_list = books_list
        self.users_list = users_list


print("Welcome to the Library Management System. Below is a list of the available options:"
 "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
 "\n 7) List available books" )

user_input = input("Please enter the number associated with the option you would like to select: ")


if user_input == str(1):
    print('You have selected the "Add book" option.')
    new_book_title = input("Please enter the title of the new book: ")