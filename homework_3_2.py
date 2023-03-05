age = int(input("Enter your age please:"))
name = input("Enter your name please:")
ageMin = 21
if age >= ageMin:
    print("Welcome to the club" + " " + name + "!")
else:
    print("Sorry" + " " + name + "," + "you are too young")