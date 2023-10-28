# Edit the same list as Exercise 4 to change your guest name who is not coming.
invitees = ["Hina","Mariyam","Ifrah"]
#print the message about the guest who can't come.
guest_cant_make_it = "Ifrah"
print(f"unfortunately, {guest_cant_make_it} can't make it to the dinner.")
#now modify the list to replace the guest who can't come with the new person you are inviting.
#We will use remove method to remove ifrah from invitees list as she is cant come for dinner.
invitees.remove(guest_cant_make_it)
# will use a variable to add new person.
new_invitee = "Anaya"
#now we will use append method to add new person name to the list.
invitees.append (new_invitee)
#Now print a second set of invitation message for the remaining guest using for loop and formatted string (f_string).
for person in invitees:
    invitation= f"Dear {person}, you are invited to my place for dinner. Please join us for a wonderful dinner."
#Finally print invitation for each person.
    print(invitation)
