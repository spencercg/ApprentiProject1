from Book import Book
from User import User
import csv

class Library:
    books_list = list
    users_list = list



    def __init__(self):
        self.books_list = books_list
        self.users_list = users_list



# These are the books that are already in the library.
'''
book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
book_1_title = book_1.title

book_2 = Book("1984", "George Orwell", "13571357", True)
book_2_title = book_2.title

book_3 = Book("Blood Meridian", "Cormac McCarthy", "45674567", True)
book_3_title = book_3.title

book_4 = Book("Catch-22", "Kurt Vonnegut", "24682468", True)
book_4_title = book_4.title


books_list = [book_1_title, book_2_title, book_3_title, book_4_title]
'''

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

user_input = input("\nPlease enter the number associated with the option you would like to select: ")


if user_input == str(1):
    print('You have selected the "Add book" option.')
    user_input_title = input("Please enter the new book's title: ")
    user_input_author = input("Please enter the new book's author: ")
    user_input_isbn = input("Please enter the new book's ISBN number: ")
    new_book = Book(user_input_title, user_input_author, user_input_isbn, True)
    new_book_title = new_book.title

    with open('available_books.csv', 'a', newline='\n') as avail_books_csvfile:
        writer = csv.writer(avail_books_csvfile)
        writer.writerow([user_input_title, user_input_author, user_input_isbn])
    
    avail_books_list = []
    with open('available_books.csv', "r") as file:

        # delimiter is the character that separates each column
        csv_reader = csv.reader(file, delimiter=",")
            
        # skip the headers with next() or a line counter
        next(csv_reader)

        for row in csv_reader: 
            # csv module automatically puts each column into a list: [Dan,Pickles,dan.pickles@email.com]
            book_title = row[0]
            avail_books_list.append(book_title)
        print("\nBelow is a list of the available book titles: ") 
        print(avail_books_list)
    
    '''
    books_list.append(new_book_title)
    print("Thank you!\n\nHere is the updated list of available books: ")
    print(books_list)
    '''
elif user_input == str(2):
    print('\nYou have selected the "Remove book" option.')
    print("\nBelow is the list of available books: ")
    
    avail_books_list = []

    with open('available_books.csv', "r") as file:

        # delimiter is the character that separates each column
        csv_reader = csv.reader(file, delimiter=",")
            
        # skip the headers with next() or a line counter
        next(csv_reader)

        for row in csv_reader: 
            book_title = row[0]
            avail_books_list.append(book_title)
        print(avail_books_list)




    bye_book_title = input("\nPlease enter the title of the book you would like to remove: ")

    with open('available_books.csv', "r+") as file:
        
        csv_reader = csv.reader(file, delimiter=",")
        
        for row in csv_reader: 
            book_title_row = row[0]
            if bye_book_title == book_title_row:
                del row
            else:
                continue
        
        for row in csv_reader: 
            book_title = row[0]
            avail_books_list.append(book_title)
        print("\nBelow is a list of the available book titles: ") 
        print(avail_books_list)    



    '''
    books_list.remove(bye_book_title)
    print("Below is the updated list of available books: ")
    print(books_list)
    '''
# Here I need to add the find and remove option for bye_book_title


elif user_input == str(3):

    print('\nYou have selected the "Add user" option.')
    
    print("\nBelow is a list of the active users: ") 

    print(users_list)




    '''
    active_users_list = []

    with open('users.csv', "r") as file:

        # delimiter is the character that separates each column
        csv_reader = csv.reader(file, delimiter=",")
            
        # skip the headers with next() or a line counter
        next(csv_reader)

        for row in csv_reader: 
            user_name = row[0]
            active_users_list.append(user_name)
        print("\nBelow is a list of the active users: ") 
        print(active_users_list)

    new_user_name = input("\nPlease enter the new user's name: ")

    new_user_id = input("\nPlease enter the new user's ID number: ")

    with open('users.csv', 'a', newline='\n') as users_csvfile:
        writer = csv.writer(users_csvfile)
        writer.writerow([new_user_name, new_user_id])
    
    active_users_list = []

    with open('users.csv', "r") as file:

        # delimiter is the character that separates each column
        csv_reader = csv.reader(file, delimiter=",")
            
        # skip the headers with next() or a line counter
        next(csv_reader)

        for row in csv_reader: 
            user_name = row[0]
            active_users_list.append(user_name)
        print("\nBelow is a list of the active users: ") 
        print(active_users_list)

    '''

elif user_input == str(4):
    print('\nYou have selected the "Remove user" option.')
    
    active_users_list = []

    with open('users.csv', "r") as file:

        # delimiter is the character that separates each column
        csv_reader = csv.reader(file, delimiter=",")
            
        # skip the headers with next() or a line counter
        next(csv_reader)

        for row in csv_reader: 
            user_name = row[0]
            active_users_list.append(user_name)
        print("\nBelow is a list of the active users: ") 
        print(active_users_list)



    bye_user_name = input("\nPlease enter the name of the user you would like to remove: ")

# Add here the means to find and remove user entry from users.csv
    '''
    users_list.remove(bye_user_name)
    print("User has been removed. Below is the updated list of users: ")
    print(users_list)
    '''

elif user_input == str(7):
    print('\nYou have selected the "List available books" option.')

    avail_books_list = []

    with open('available_books.csv', "r") as file:

        # delimiter is the character that separates each column
        csv_reader = csv.reader(file, delimiter=",")
            
        # skip the headers with next() or a line counter
        next(csv_reader)

        for row in csv_reader: 
            book_title = row[0]
            avail_books_list.append(book_title)
        print("\nBelow is a list of the available book titles: \n") 
        print(avail_books_list)

else:
    print('\nInvalid input. \n\nPlease select from the list of available options: '
    '\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book' 
    '\n 7) List available books')










