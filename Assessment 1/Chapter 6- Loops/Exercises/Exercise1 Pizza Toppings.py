# write a loop that prompts user to enter pizza toppings.we will use while loop statement until they enter 'quit' value.
topping=""
while True:
    topping= input("Enter a pizza topping (type 'quit' to finish):")
# If topping is  equal to 'quit' it will print the following statement.
    if topping== 'quit':
        print("Exiting pizza topping selection. Enjoy your pizza!")
# we write break to exits the loop.
        break
# when a user inputs topping it will print the following statement.
    print(f"Adding {topping} to your pizza.")
