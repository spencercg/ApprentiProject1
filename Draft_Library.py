from Book import Book
from User import User

'''
# These are the books that are in the library and available to be checked out.

book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
book_2 = Book("1984", "George Orwell", "13571357", True)
book_3 = Book("Blood Meridian", "Cormac McCarthy", "45674567", True)
book_4 = Book("Catch-22", "Kurt Vonnegut", "24682468", True)


# These are the books that are currently checked out.

book_5 = Book("Brave New World", "Aldous Huxley", "23452345", False)

book_6 = Book("The Divine Invasion", "Philip K. Dick", "34563456", False)

book_7 = Book("The Magic Mountain", "Thomas Mann", "56785678", False)

 

books_str_list = [book_1.__str__(), book_2.__str__(), book_3.__str__(), book_4.__str__(), book_5.__str__(), 
                  book_6.__str__(), book_7.__str__()]

# books_list = [book_1, book_2, book_3, book_4]

books_list = [book_1, book_2, book_3, book_4, book_5, book_6, book_7]

checked_out_master_list_str = []




# checked_out_master_list = [book_5, book_6, book_7]

checked_out_master_list = []


# These are the Users that are already in the Library system.

user_1 = User("Abigail", "0001", [book_5.title])
user_2 = User("Betty", "0002", [book_6.title])
user_3 = User("Christian", "0003", [book_7.title])


users_list = [user_1, user_2, user_3]

users_str_list = [user_1.__str__(), user_2.__str__(), user_3.__str__()]
'''


class Library:
    books_list = list
    users_list = list

    def add_book():
        print('\nYou have selected the "Add book" option.')
        user_input_title = input("\nPlease enter the new book's title: ")
        user_input_author = input("\nPlease enter the new book's author: ")
        user_input_isbn = input("\nPlease enter the new book's eight digit ISBN number: ")
        new_book = Book(user_input_title, user_input_author, user_input_isbn, True)
        new_book_title = new_book.title
        
        books_str_list.append(new_book_title)
        print()
        print(new_book_title + " has been successfully added.")
        print("\nHere is the updated list of available books: ")
        print(books_str_list)

        books_list.append(new_book)
            
    def remove_book():

        print('\nYou have selected the "Remove book" option.')
        print("\nBelow is the list of available books: ")
    
        print(books_str_list)

        bye_book_title = input("\nPlease enter the title of the book you would like to remove: ")

        if bye_book_title in books_str_list:

            books_str_list.remove(bye_book_title)
            print()
            print(bye_book_title + " has been removed.")
            print("\nBelow is the updated list of available books: ")
            print(books_str_list)
        
        else:
            print("\nTitle not found. Please try again.")

    def add_user():
        print('\nYou have selected the "Add user" option.')
    
        print("\nBelow is a list of the active users: ") 

        print(users_str_list)

        user_input_name = input("\nPlease enter the new user's name: ")

        user_input_id = input("\nPlease enter the new user's four digit ID number: ")

        new_user = User(user_input_name, user_input_id, [])
        new_user_name = new_user.name

        users_str_list.append(new_user_name)
        print()
        print(new_user_name + " has been successfully added.")
        print("\nHere is the updated list of active users: ")
        print(users_str_list)

        users_list.append(new_user)

    def remove_user():
        print('\nYou have selected the "Remove user" option.')
    
        print("\nBelow is a list of the active users: ") 
        print(users_str_list)

        bye_user_name = input("\nPlease enter the name of the user you would like to remove: ")

        if bye_user_name in users_str_list:
            users_str_list.remove(bye_user_name)
            print()
            print(bye_user_name + " has been removed.")
            print("\nBelow is the updated list of users: ")
            print(users_str_list)
        else:
            print('\nUser not found. Please select "Remove user" option and try again.')

    def borrow_book():

        print('\nYou have selected the "Borrow book" option.')  

        print('\nBelow is a list of the available books: ')
        print(books_str_list)
        borrow_book_title = input("\nPlease enter the title of the book to be borrowed: ")
                   
        
        if borrow_book_title in books_str_list:
            print("\nRequested title to be borrowed is " + borrow_book_title + ".")
       

            print('\nBelow is a list of the active users: ')
            print(users_str_list)
            borrow_user_name = input("\nPlease enter the name of the user requesting to borrow the book: ")
        

            if borrow_user_name in users_str_list:
                
                print("\nRequested borrower is " + borrow_user_name + ".")
                print()
                print(borrow_book_title + " has been successfully borrowed by " + borrow_user_name + ".")
                
                

                for i in books_str_list:
                    if i == borrow_book_title:
                        index = books_str_list.index(i)
                        books_list[index].borrow_book()
                        books_str_list.remove(i)
                        
                        

                
                        # print(books_list[index].available)
                        print()

                    else:
                        continue

                for j in users_str_list:
                    if j == borrow_user_name:
                        index = users_str_list.index(j)
                        users_list[index].borrow_book(borrow_book_title)
                        print(borrow_user_name + " is currently borrowing the following books: ")
                        # print(users_list[index].borrowed_books)
                        print(users_list[index].view_borrowed_books())
                    else:
                        continue

                       
            else:
                print("\nInvalid input. Please try again.")
    
        else:
            print("\nInvalid input. Please try again.")

    def return_book():
        
        print('\nYou have selected the "Return book" option.')

        for m in books_list:
            if m.available == False and m.title not in checked_out_master_list:
                checked_out_master_list.append(m)
            else:
                continue


        for n in checked_out_master_list:
            str_title = n.__str__()
            if str_title not in checked_out_master_list_str:
                checked_out_master_list_str.append(str_title)
                # print(checked_out_master_list_str)
            else:
                continue

        print('\nBelow is a list of the books that can be returned: ')

        print(checked_out_master_list_str)

        book_to_return = input("\nPlease enter the title of the book you would like to return: ")


        for b in users_list:
            if book_to_return in b.borrowed_books:
                print()
                print(b.name + " is returning " + book_to_return + ".")
                b.return_book(book_to_return)
                print("\nThank you for returning " + book_to_return + "!")
            else:
                continue


               
        if book_to_return in checked_out_master_list_str:
            checked_out_master_list_str.remove(book_to_return)
            print(checked_out_master_list_str)
            # print(checked_out_master_list)

        else:
            print("Please enter a valid title.")

        for p in checked_out_master_list:
            if p.title == book_to_return:
                p.return_book()
                # print(p.available)
                if p.title not in books_list:
                    books_list.append(p)
                    returned_book_title = p.__str__()
                    if returned_book_title not in books_str_list:
                        books_str_list.append(returned_book_title)
                    else:
                        continue
                else:
                    continue

            else:
                continue

        
        '''
        if book_to_return in checked_out_master_list_str:
            checked_out_master_list_str.remove(book_to_return)
            # print(checked_out_master_list_str)
        else:
            print("\nInvalid input. Please try again.")
        '''

        '''
        for q in checked_out_master_list:
            print(q.title)
                if p.title == book_to_return:
                    p.return_book()
                    # print(p.available)
                    if p.title not in books_list:
                        books_list.append(p)
                        returned_book_title = p.title.__str__()
                        if returned_book_title not in books_str_list:
                            books_str_list.append(returned_book_title)
                        else:
                            continue
                    else:
                        continue

                else:
                    continue
                    '''
                    

    def list_available_books():
        print('\nYou have selected the "List available books" option.')
        print("\nBelow is a list of the available books: ")
        print()
        books_available_list = []
        for v in books_list:
            if v.available == True:
                books_available_list.append(v.title)
        print(books_available_list)


    def __init__(self):
        self.books_list = books_list
        self.users_list = users_list


# These are the books that are in the library and available to be checked out.

book_1 = Book("Moby Dick", "Herman Melville", "12341234", True)
book_2 = Book("1984", "George Orwell", "13571357", True)
book_3 = Book("Blood Meridian", "Cormac McCarthy", "45674567", True)
book_4 = Book("Catch-22", "Kurt Vonnegut", "24682468", True)


# These are the books that are currently checked out.

book_5 = Book("Brave New World", "Aldous Huxley", "23452345", False)

book_6 = Book("The Divine Invasion", "Philip K. Dick", "34563456", False)

book_7 = Book("The Magic Mountain", "Thomas Mann", "56785678", False)

 

books_str_list = [book_1.__str__(), book_2.__str__(), book_3.__str__(), book_4.__str__(), book_5.__str__(), 
                  book_6.__str__(), book_7.__str__()]

# books_list = [book_1, book_2, book_3, book_4]

books_list = [book_1, book_2, book_3, book_4, book_5, book_6, book_7]

checked_out_master_list_str = []




# checked_out_master_list = [book_5, book_6, book_7]

checked_out_master_list = []


# These are the Users that are already in the Library system.

user_1 = User("Abigail", "0001", [book_5.title])
user_2 = User("Betty", "0002", [book_6.title])
user_3 = User("Christian", "0003", [book_7.title])


users_list = [user_1, user_2, user_3]

users_str_list = [user_1.__str__(), user_2.__str__(), user_3.__str__()]



# Welcome screen for the Library Management Systemm

print("\nWelcome to the Library Management System. \n\nBelow is a list of the available options:\n"
 "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
 "\n 7) List available books\n 0) Quit program" )


user_input = input("\nPlease enter the number associated with the option you would like to select: ")


while user_input != str(0):


    if user_input == str(1):

        Library.add_book()

        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")

    
    elif user_input == str(2):

        Library.remove_book()

        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")


    elif user_input == str(3):

        Library.add_user()
        
        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")
        

    elif user_input == str(4):

        Library.remove_user()

        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")
        

    elif user_input == str(5):

        Library.borrow_book()

        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")


    elif user_input == str(6):
        
        Library.return_book()

        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")
    

    elif user_input == str(7):
        Library.list_available_books()
        
        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")


    else:
        
        print('\nInvalid input. Please try again and select from list of available options.\n')
        
        print("\nWelcome to the Library Management System. Below is a list of the available options:"
                "\n 1) Add book \n 2) Remove book \n 3) Add user \n 4) Remove user \n 5) Borrow book \n 6) Return book" 
                "\n 7) List available books\n 0) Quit program" )
    
        user_input = input("\nPlease enter the number associated with the option you would like to select: ")

        


if user_input == str(0):
    print("\nThank you for using the Library Management System!\n")








