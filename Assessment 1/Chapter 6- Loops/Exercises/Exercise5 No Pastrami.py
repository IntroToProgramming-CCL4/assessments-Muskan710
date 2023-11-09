#We will create a sandwich_orders list
sandwich_orders = ['Grilled cheese','Nutella','Grilled chicken','Pastrami','Pastrami','Pastrami']

#Now we will create finished_sandwiches list.
finished_sandwiches = []
# it will print the following message if pastrami is not in list.
print("Sorry, The deli has run out of pastrami.")
# we use remove method to remove pastrami from the list when the while will check for it .
while 'Pastrami'in sandwich_orders:
    sandwich_orders.remove('Pastrami')

##The append()method is used to add an element to end of the list and it will be add to finished_sandwiches list after printing the statement.
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

#printing finished sandwiches list .
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)