# we will use while loop to keep asking the user for his/her age.
Age=""
while True:
    age = int(input("How old are you?"))
#If the person age is less than 3 it will print the following statement.
    if age < 3:
        print("Your ticket is free!")
#If the person age is between 3 and 12 it will print elif statement.or if it is over than 12 it will print else statement.
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
        break
