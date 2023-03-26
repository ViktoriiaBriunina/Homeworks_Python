import os
import datetime

user_info = {}

today = datetime.date.today().strftime('%Y-%m-%d')

if not os.path.exists(today):
    os.makedirs(today)

while True:
    name = input("Please, enter your name: ")
    surname = input("Please, enter your surname: ")
    ID = input("Please, enter your personal code: ")

    user = {"Name": name, "Surname": surname}
    user_info[ID] = user

    file_name = f"{ID}.txt"
    file_path = os.path.join(today, file_name)
    with open(file_path, 'w') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Surename: {surname}\n")
        f.write(f"ID Number: {ID}\n")

    choice = input("Enter 'n' to exit : ")
    if choice == 'n':
        break

for ID, user in user_info.items():
    print(f"ID Number: {ID}")
    print(f"Name: {user['Name']}")
    print(f"Age: {user['Surname']}")
    print("-------------------------------------------")





