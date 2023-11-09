#choose a color for an alien and write an if- else chain.
# Here we ask the user to input the color.
alien_colors =input("Enter the color of the alien ('green','Red','yellow'):")

#we use double equal sign (==) to see if the color of alien is green.
if alien_colors == 'green':
# if it is green it should print the following statement.
    print("The player just earned 5 points for shooting the alien")
else:
#if the color is not green. 
    print("The palyer just earned 10 points")

