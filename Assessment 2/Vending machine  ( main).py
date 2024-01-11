import os

item01= {'code':'A01',"name":"Greek salad        ","price":8.0,'category':"Cuisine"}
item02= {'code':'A02',"name":"Mini pizza         ","price":5.0,'category':"Cuisine"}
item03= {'code':'A03',"name":"Tacos              ","price":8.0,'category':"Cuisine"}
item04= {'code':'A04',"name":"Dumpling           ","price":6.0,'category':"Cuisine"}
item05= {'code':'A05',"name":"Croissant          ","price":3.5,'category':"Cuisine"}    
item06= {'code':'B01',"name":"break chocolate    ","price":5.0,'category':"chocolate"}
item07= {'code':'B02',"name":"galaxy chocolate   ","price":8.0,'category':"chocolate"}
item08= {'code':'B03',"name":"nutella chocolate  ","price":7.0,'category':"chocolate"}
item09= {'code':'B04',"name":"snickers chocolate ","price":8.0,'category':"chocolate"}
item10= {'code':'B05',"name":"kitkat chocolate   ","price":4.0,'category':"chocolate"}   
item11= {'code':'C01',"name":"Mango juice        ","price":5.0,'category':"juice"}
item12= {'code':'C02',"name":"Apple juice        ","price":3.0,'category':"juice"}
item13= {'code':'C03',"name":"orange juice       ","price":6.0,'category':"juice"}
item14= {'code':'C04',"name":"banana juice       ","price":5.0,'category':"juice"}
item15= {'code':'C05',"name":"kiwi juice         ","price":4.0,'category':"juice"}   
item16= {'code':'D01',"name":"pide               ","price":8.0,'category':"Tukish cuisine"}
item17= {'code':'D02',"name":"kebab              ","price":8.0,'category':"Tukish cuisine"}
item18= {'code':'D03',"name":"lentil soup        ","price":5.0,'category':"Tukish cuisine"}
item19= {'code':'D04',"name":"turkish tea        ","price":6.0,'category':"Tukish cuisine"}
item20= {'code':'D05',"name":"baklava            ","price":9.5,'category':"Tukish cuisine"}       
item21= {'code':'E01',"name":"coka cola          ","price":3.0,'category':"Beverages"}
item22= {'code':'E02',"name":"water              ","price":2.0,'category':"Beverages"}
item23= {'code':'E03',"name":"7up                ","price":3.0,'category':"Beverages"}
item24= {'code':'E04',"name":"tea                ","price":2.0,'category':"Beverages"}
item25= {'code':'E05',"name":"coffee             ","price":4.0,'category':"Beverages"}

items =[item01,item02,item03,item04,item05,item06,item07,item08,item09,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25]

# Clear screen will help in making the output neat
def clear_screen(): 
    os.system('clear' if os.name == 'posix' else 'cls')


def print_menu():   # this function print Menu  which will print the items in proper order
    print("="*38)
    print(f"CODE\tITEM\t\t\tPRICE\t")
    for item in items:
        print(f"{item['code']}\t{item['name']}\t{item['price']}\t")
    print("="*38)



def display_cart(cart):  # this will help in keeping the cart[] data organized 
    print("-"*34)
    print("\n These Items are in your cart:")
    print("-"*34)
    for item in cart:
        
        print(f"{item['code']}\t{item['name']}{item['price']}\t")
    print("="*34)
    

# This function will be user to add more items in user cart
def add_more_items():
    while True:
        Ask_user_item = input("Would you like to add another item? Enter (E) for Yes And (O) For No: ").lower()
        if Ask_user_item in ['yes', 'e']:
            return True
        elif Ask_user_item in ['no', 'o']:
            clear_screen()
            return False
        else:
            print("Please enter Yes or No.")

# it will ask the user for money and and return change 
def Enter_money(total_cost):
    total_amount = 0
    print("\nEnter Money:")
    while True:
        try:
            amount = float(input("Enter money: "))
            if amount < 0:
                print("Invalid amount. Please enter a valid number.")
            else:
                total_amount += amount
                if total_amount >= total_cost:
                    change = total_amount - total_cost
                    print(f"Total Paid: ${total_amount}. Your change: ${change:.2f}")
                    return total_amount, change
                else:
                    print(f"Total Paid: ${total_amount}. Amount still needed: ${total_cost - total_amount}")
        except ValueError:
            print("Invalid input. Please insert a valid number.")

# this will give the sum of all the items in user cart
def process_cart_payment(cart):
    total_cost = sum(item['price'] for item in cart)
    print(f"Total Cost of your order: ${total_cost}")
    total_amount, change = Enter_money(total_cost)
    return total_amount, change

#This will print the reciept in organized manner
def user_payment_receipt(total_amount, cart):
    print("="*30)
    print("    This is your receipt")
    print("="*30)
    for item in cart:
        print(f"{item['name']}\t${item['price']}")
    print("="*30)
    print(f"Total Price \t\t${sum(item['price'] for item in cart)}")
    print("="*30)
    print(f"Amount paid \t\t${total_amount:.2f}\t")
    print(f"Your change\t\t${total_amount - sum(item['price'] for item in cart):.2f}")
    print("="*30)
    print("Have a Wonderful day!")
    print("="*30)


def ask_for_receipt():  # this will give user an option if the want reciept or no 
    while True:
        Ask_user = input("Would you like to take a receipt? (Y) for yes & (N) for NO: ").lower()
        if Ask_user in ['yes', 'y']:
            return True
        elif Ask_user in ['no', 'n']:
            return False
        else:
            print("Please enter Yes or No.")


def get_user_input(): # this is the main lop in which the user will enter code of product and handle all the process of the vending machione 
    cart = []   # empty list where all the user order will be saved 

    while True:
        # this wil give user input to enter item code tjey wanna buy
        user_input = input("Enter item code (or 'exit' to quit):").upper()
        found = False   
        # this will check if the code entered matches with the items list
        for item in items:
            if user_input == item['code']:
                clear_screen()
                print_menu()
                cart.append(item)  # append will add items to the empty lis called cart[]
                display_cart(cart)  # This will display the updated cart 
                 
                if not add_more_items():  # it will check if the user wishes to add more items to cart
                    # if no more items to be added then this will process with the payment
                    total_amount, change = process_cart_payment(cart)
                    Reciept_For_User = ask_for_receipt()
                    clear_screen()
                    if Reciept_For_User:
                        user_payment_receipt(total_amount, cart)
                    print("Thank You for your purchase")
                    return
                else:
                    found = True
                    break  
         
        if user_input == 'EXIT': # This will handle exit input for ending program 
            print("Have a good day")
            break
        elif not found and user_input != 'EXIT':
            print("Invalid code")

# this will Run the program: prints menu ,clear_screen and get started with user input process
clear_screen()
print_menu()
get_user_input() 