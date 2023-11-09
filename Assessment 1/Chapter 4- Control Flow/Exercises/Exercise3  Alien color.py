#turn your if-else chain into  if-elifelse chain.
#we ask the user to input the color of an alien.
alien_color= input("Enter the alien color('green','yellow',or 'red'):")

#if the color is equal to green.
if alien_color =='green':

#it will print the following statement.
    print("The palyer earned 5 points for shooting the alien.")

#if the was equal to yellow it will execute the elif block.
elif alien_color =='yellow':

# printing the following statement.
    print("The player earned 10 points.")

#it will execute the elif block if it was equal to red.
elif alien_color =='red':

# printing the following stetmant.
    print("The palyer earned 15 points.")

#otherwise if none of the above colors were equal it will execute the else block.
else: 
    print("Invalid alien color.please choose from green,yellow,or red.")