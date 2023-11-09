# we will use the def statement for this program.
def make_shirt(size,message):
    print(f"Making a shirt of size {size} with the message: '{message}' ")

#calling the function with positional arguments.
make_shirt("Medium","Last Bear")

#calling the function with keyword arguments.
make_shirt(size="Large",message="Lost sea")
