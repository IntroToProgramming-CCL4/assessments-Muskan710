#We will create a sandwich_orders list
sandwich_orders = ['Grilled cheese','Nutella','Grilled chicken']

#Now we will create finished_sandwiches list
finished_sandwiches = []

#now loop through the sandwich_orders 
for sandwich in sandwich_orders:
#printing statement for each sandwich using formatted_text (f)
    print(f"I made your {sandwich} sandwich.")

#The append()method is used to add an element to end of the list and it will be add to finished_sandwiches list after printing the statement.
    finished_sandwiches.append(sandwich)

#Now printing the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
