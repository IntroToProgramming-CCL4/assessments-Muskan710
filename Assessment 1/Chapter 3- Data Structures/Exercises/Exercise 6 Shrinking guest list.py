#we create a list of friends thats to be inivited for dinner.
invitees = ["Hina","Mariyam","ifrah","Anaya"]
#we will use print statement to inform that only two people can be invited due to the delay of dinner table.
print("unfortunately,the dinner table won't arrive on time, therefore we can only invite two people for dinner.")
#we use while loop to remove guests from the invitees list using pop() method.
while len(invitees) > 2:
#The loop continues until only two names remain in the list.
    removed_person = invitees.pop()
#creating a sorry message for people who is removed from the list.
    print(f"Sorry,{removed_person},we can't invite you to dinner.")
#now we have create a message to each of the two person who are still on list using for loop.
for person in invitees:
    print(f"Dear {person},you are still invited for dinner at my place. Please join us for a wonderful dinner.")
#Now we will use del to remove last two names from our list.
del invitees[0] #remove the first remaining person
del invitees[0] #remove the second remaining person
#print your list to make sure you have an empty list.
print("Updated list of invitees:",invitees)


