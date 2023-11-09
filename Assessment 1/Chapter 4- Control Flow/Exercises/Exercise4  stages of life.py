# write an if-elif-else chain that determines a person's stage of life.
# we will asign a value to the variable (age).
age=30

# now we will check if the person age is less than 2.
if age < 2:
#it will print the following statement.
    print("The person is baby.")

# otherwise it will print the following statament using else if(elif) when the first statement isn't true.
elif age <4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20 :
    print("The person is a teenager.")
elif age < 65 :
    print("The person is an adult.")

# and if the person age is more than 65 it will print the following statement using else statement.
else:
    print("The person is an elder.")
