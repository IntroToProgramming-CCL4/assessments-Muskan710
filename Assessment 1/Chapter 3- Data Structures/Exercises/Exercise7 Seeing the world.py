# create a list of places you would like to vist but should not be in alphabetical order.
places_to_visit= ["Paris","Maldives","London","Rome","Finland"]

# print your list in its original order
# the original list is printed as it is.
print("original list:",places_to_visit)

#Use sorted() to print the list in alphabetical order without modifying the actual list.
print("alphabetical list:",sorted (places_to_visit))

#show that the original list is still in its original order by printing it.
print("original list (again):", places_to_visit)

#use sorted() to print the list in reverse alphabetical order without changing the order of the original list.
print("reverse alphabetical list :" ,sorted(places_to_visit,reverse=True))

#show that the original list is still in its original order by printing it again.
print("original list(again):", places_to_visit)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
places_to_visit.reverse()
print("reverse list (again)" ,places_to_visit)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places_to_visit.reverse()
print("original list (again):",places_to_visit)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places_to_visit.sort()
print("alphabatical list:",places_to_visit)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places_to_visit.sort(reverse=True)
print("reverse alphabatical list:",places_to_visit)

