# Create dictionary to represents a different pet include kind of animal and the owners name.
pet1={"kind":"cat","owner":"Joye","color":"white","age":"2year's"}
pet2={"kind":"Dog","owner":"Max","color": "Black","age":"4year's"}
pet3={"kind":"Parrot","owner":"Bob","color":"Green","age":"5 days"}
pet4={"kind":"Hamster","owner":"Alice","color":"Red","age":"10 days"}
pet5={"kind":"Fish","owner":"Anaya","color":"Blue","age":"1 month"}

#now we will store the dictionaries in a list called  as "pets"
pets=[pet1,pet2,pet3,pet4,pet5] 

#Next, We  have  to loop through owr list and as we do,  and print everything you know about each pet.
for pet in pets:
    print(f" The kind of pet is :{pet['kind']}")
    print(f"It's owner's name is :{pet['owner']}")
    print(f" The color of the pet is :{pet['color']}")
    print(f"This pet is:{pet['age']} old")
