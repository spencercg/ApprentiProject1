import csv

class User:
    name: str
    user_id: str
    borrowed_books = list

    def __init__(self, name, user_id, borrowed_books):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = borrowed_books


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

print(user_list[0].borrowed_books)
    
