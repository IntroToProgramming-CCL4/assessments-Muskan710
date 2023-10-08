#write a programme that accept radius of circle from the user and compute area.
#import the math module for pi operation.
import math as M 
# float is used to write both whole and decimal numbers.the user will input the radius in output.
Radius=float(input(" enter the radius of the given circle:"))
#Now write formula for the area of circle.
area_of_the_circle= M.pi * Radius * Radius
#Now print the area of circle.
print("The area of the given circle:", area_of_the_circle)
