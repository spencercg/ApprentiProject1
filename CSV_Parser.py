import csv

class User:
    name: str
    user_id: str
    borrowed_books = list

    def __init__(self, name, user_id, borrowed_books):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = borrowed_books

'''
with open("users.csv") as file:
    reader = csv.reader(file, delimiter=',')
    user_list = []
    row_number = 1
    for list in reader:
        if row_number != 1:
            user = User(list[0], list[1], list[2:])
            user_list.append(user)
            row_number += 1
        else:
            row_number += 1


user_list.append(User("Daniel", "0004", "Moby Dick"))

print(user_list[1].borrowed_books)
 '''   

with open('users.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    


    # writer.writerow(['Jacob', '0015', 'Doors of Perception'])
'''  
with open("available_books.csv") as file:
        reader = csv.reader(file, delimiter=',')
        book_list = []
        row_number = 1
        for list in reader:
            if row_number != 1:
                book = Book(list[0], list[1], list[2:], True)
                book_list.append(book)
                row_number += 1
            else:
                row_number += 1
            print(book.title)
            '''