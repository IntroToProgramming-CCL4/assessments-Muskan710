# write a program to calculate how many USB sticks she can buy and how many pounds she will have left.
# define the girls budget and the cost of each USB stick.
budget = 50 #£ 50 
usb_stick_cost = 6 #£6 each 
# we use a variable to store the result usb_sticks_purchased and pounds_left.
# We use the integer division (//) operator to calculate how many USB sticks she can buy.
# This operator divides the buget by the cost of each USB stick and will returns the whole number of USB sticks she can purchase.
usb_sticks_purchased = budget // usb_stick_cost 
# Now calculate how many pounds she will have left.
# we use (%) operator to give us the remainder after dividing the budget by the cost of each USB stick.
pounds_left = budget % usb_stick_cost 
#display output.
print("The girl can buy", usb_sticks_purchased ," USB sticks. ")
print("She will have £", pounds_left, "left.")
#Now print statement is used to display the numbers of USB sticks buyed and how many pounds she will be left with. 




