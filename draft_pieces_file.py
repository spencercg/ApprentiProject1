


        '''
    print('You have selected the "Add book" option.')
    user_input_title = input("Please enter the new book's title: ")
    user_input_author = input("Please enter the new book's author: ")
    user_input_isbn = input("Please enter the new book's ISBN number: ")
    new_book = Book(user_input_title, user_input_author, user_input_isbn, True)
    new_book_title = new_book.title

    books_list.append(new_book_title)
    print("Thank you!\n\nHere is the updated list of available books: ")
    print(books_list)
        '''


 '''
    print('\nYou have selected the "Remove book" option.')
    print("\nBelow is the list of available books: ")
    
    print(books_list)

    bye_book_title = input("\nPlease enter the title of the book you would like to remove: ")

    books_list.remove(bye_book_title)
    print("Below is the updated list of available books: ")
    print(books_list)
        '''

'''
    print('\nYou have selected the "Add user" option.')
    
    print("\nBelow is a list of the active users: ") 

    print(users_list)

    user_input_name = input("\nPlease enter the new user's name: ")

    user_input_id = input("\nPlease enter the new user's ID number: ")

    new_user = User(user_input_name, user_input_id, [])
    new_user_name = new_user.name

    users_list.append(new_user_name)
    print("Thank you!\n\nHere is the updated list of active users: ")
    print(users_list)
        '''

'''
    print('\nYou have selected the "Remove user" option.')
    
    print("\nBelow is a list of the active users: ") 
    print(users_list)

    bye_user_name = input("\nPlease enter the name of the user you would like to remove: ")

    if bye_user_name in users_list:
        users_list.remove(bye_user_name)
        print("\nUser has been removed. Below is the updated list of users: ")
        print(users_list)
    else:
        print('\nUser not found. Please select "Remove user" option and try again.')
        '''




'''
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
                        print(users_list[index].borrowed_books)

                       
            else:
                print("\nInvalid input. Please try again.")
    
        else:
            print("\nInvalid input. Please try again.")
            '''




 '''
        print('\nYou have selected the "Return book" option.')  

        print('\nBelow is a list of the books that can be returned: ')

        checked_out_list = []
    
        for k in users_list:
            checked_out_book = k.borrowed_books

            str_chk_out_book = checked_out_book[0]
            
            checked_out_list.append(str_chk_out_book)
            
        print(checked_out_list)

        book_to_return = input("\nPlease enter the title of the book you would like to return: ")

        if book_to_return in checked_out_list:
            print("\nYou have selected to return " + book_to_return)
            for m in checked_out_master_list:
                if m.title == book_to_return:
                    m.return_book()
                    books_list.append(m)
                    books_str_list.append(m.title)
                    print("\nBelow is a list of the available books: ")
                    print()
                    print(books_str_list)
                else:
                    continue


        else:
            print("Invalid input. Please try again.")
                '''


    '''
        for k in users_list:
            checked_out_book = k.borrowed_books

            str_chk_out_book = checked_out_book[0]
            
            checked_out_list.append(str_chk_out_book)
            
        print(checked_out_list)

        book_to_return = input("\nPlease enter the title of the book you would like to return: ")

        if book_to_return in checked_out_list:
            print("\nYou have selected to return " + book_to_return)
            for m in checked_out_master_list:
                if m.title == book_to_return:
                    m.return_book()
                    books_list.append(m)
                    books_str_list.append(m.title)
                    print("\nBelow is a list of the available books: ")
                    print()
                    print(books_str_list)
                else:
                    continue


        else:
            print("Invalid input. Please try again.")        
        '''


        '''

        for k in users_list:
            checked_out_book = k.borrowed_books

            str_chk_out_book = checked_out_book[0]
            
            checked_out_list.append(str_chk_out_book)
            
        print(checked_out_list)

        book_to_return = input("\nPlease enter the title of the book you would like to return: ")

        if book_to_return in checked_out_list:
            print("\nYou have selected to return " + book_to_return)
            for m in checked_out_master_list:
                if m.title == book_to_return:
                    m.return_book()
                    books_list.append(m)
                    books_str_list.append(m.title)
                    print("\nBelow is a list of the available books: ")
                    print()
                    print(books_str_list)
                else:
                    continue


        else:
            print("Invalid input. Please try again.")        
        '''


'''
    print('You have selected the "Add book" option.')
    user_input_title = input("Please enter the new book's title: ")
    user_input_author = input("Please enter the new book's author: ")
    user_input_isbn = input("Please enter the new book's ISBN number: ")
    new_book = Book(user_input_title, user_input_author, user_input_isbn, True)
    new_book_title = new_book.title

    books_list.append(new_book_title)
    print("Thank you!\n\nHere is the updated list of available books: ")
    print(books_list)
        '''


'''
    print('\nYou have selected the "Remove book" option.')
    print("\nBelow is the list of available books: ")
    
    print(books_list)

    bye_book_title = input("\nPlease enter the title of the book you would like to remove: ")

    books_list.remove(bye_book_title)
    print("Below is the updated list of available books: ")
    print(books_list)
        '''

        '''
    print('\nYou have selected the "Add user" option.')
    
    print("\nBelow is a list of the active users: ") 

    print(users_list)

    user_input_name = input("\nPlease enter the new user's name: ")

    user_input_id = input("\nPlease enter the new user's ID number: ")

    new_user = User(user_input_name, user_input_id, [])
    new_user_name = new_user.name

    users_list.append(new_user_name)
    print("Thank you!\n\nHere is the updated list of active users: ")
    print(users_list)
        '''

        '''
    print('\nYou have selected the "Remove user" option.')
    
    print("\nBelow is a list of the active users: ") 
    print(users_list)

    bye_user_name = input("\nPlease enter the name of the user you would like to remove: ")

    if bye_user_name in users_list:
        users_list.remove(bye_user_name)
        print("\nUser has been removed. Below is the updated list of users: ")
        print(users_list)
    else:
        print('\nUser not found. Please select "Remove user" option and try again.')
        '''


        '''
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
                        print(users_list[index].borrowed_books)

                       
            else:
                print("\nInvalid input. Please try again.")
    
        else:
            print("\nInvalid input. Please try again.")
            '''


        '''
        print('\nYou have selected the "Return book" option.')  

        print('\nBelow is a list of the books that can be returned: ')

        checked_out_list = []
    
        for k in users_list:
            checked_out_book = k.borrowed_books

            str_chk_out_book = checked_out_book[0]
            
            checked_out_list.append(str_chk_out_book)
            
        print(checked_out_list)

        book_to_return = input("\nPlease enter the title of the book you would like to return: ")

        if book_to_return in checked_out_list:
            print("\nYou have selected to return " + book_to_return)
            for m in checked_out_master_list:
                if m.title == book_to_return:
                    m.return_book()
                    books_list.append(m)
                    books_str_list.append(m.title)
                    print("\nBelow is a list of the available books: ")
                    print()
                    print(books_str_list)
                else:
                    continue


        else:
            print("Invalid input. Please try again.")
                '''

        '''
    print('\nYou have selected the "List available books" option.')

    print(books_list)
        '''