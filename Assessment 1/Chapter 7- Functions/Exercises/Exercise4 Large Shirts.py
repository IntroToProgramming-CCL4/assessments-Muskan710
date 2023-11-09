#write a programme to modify the make-shirt.
def make_shirt(size="Large", message="I love Python"):
    print(f"Making a shirt of size {size} with the message:'{message}'")

#Now making a large shirt with the default message.
make_shirt()

#And now make medium shirt with default message.
make_shirt(size="Medium")

# And now lets make a custom-sized shirt with different message.
make_shirt(size="Small", message="Coding is fun!")