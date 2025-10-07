#Lets make concession stand!
#More like a list of food with prices
#Then we can add to it, remove from it, and update prices
#Finally we can print the list out nicely formatted

menu = {
    "Hot Dog": 2.50,
    "Burger": 3.00,
    "Fries": 1.50,
    "Soda": 1.00,
    "Candy": 0.75
}   
def print_menu():
    print("Concession Stand Menu")
    print("--------Menu---------")
    for item, price in menu.items():
        print(f"{item:.<20} ${price:.2f}")
    print("---------------------")
def add_item(item, price):
    if item in menu:
        print(f"{item} already exists in the menu.")
    else:
        menu[item] = price
        print(f"Added {item} with price ${price:.2f} to the menu.")
def remove_item(item):
    if item in menu:
        del menu[item]
        print(f"Removed {item} from the menu.")
    else:
        print(f"{item} not found in the menu.")
def update_price(item, price):
    if item in menu:
        menu[item] = price
        print(f"Updated {item} to new price ${price:.2f}.")
    else:
        print(f"{item} not found in the menu.")
#Example usage
print_menu()

# You can uncomment these to test adding, removing, and updating items:

#add_item("Ice Cream", 2.00)
#remove_item("Candy")
#update_price("Burger", 3.50)
#print_menu()

#Its like a mini database/dictionary for a concession stand!
#We can add, remove, update, and print items with prices!

#Lets add choosing your own input from menu and getting a total!
#we need to make sure user can use small or capital letters
#for hot dog, maybe we can add special function about spaces too so user can write hotdog or hot dog
#we can also add tax to the total at the end

def get_order():
    total = 0
    print("Please enter the items you want to order. Type 'done' when finished.")
    while True:
        item = input("Enter item: ").strip().title()
        if item.lower() == 'done':
            break
        if item in menu:
            total += menu[item]
            print(f"Added {item} to your order. Current total: ${total:.2f}")
        else:
            print(f"{item} is not on the menu. Please choose another item.")
    tax = total * 0.07  # Assuming a 7% sales tax
    total_with_tax = total + tax
    print(f"Your total before tax is: ${total:.2f}")
    print(f"Sales tax (7%): ${tax:.2f}")
    print("---------------------")
    print(f"Your total after tax is: ${total_with_tax:.2f}")
get_order()


#For someone who wants to make a version of this with can work with 'hottdog' istead of 'hot dog'
#We can use another secret menu dictionary that has all the possible variations of the item names
#Lastly we will make internal function to convert user input to the correct menu item name
#This way we can have a more flexible input system while keeping the menu clean and easy to read
#This is a bit more advanced but can be fun to implement!

#Here is how we can do it:

alternate_names = {
    "hotdog": "Hot Dog",
    "hot dog": "Hot Dog",
    "burger": "Burger",
    "fries": "Fries",
    "soda": "Soda",
    "candy": "Candy",
    "icecream": "Ice Cream",
    "ice cream": "Ice Cream"
}
def normalize_item_name(user_input):
    key = user_input.replace(" ", "").lower()
    return alternate_names.get(key, None)
def get_order_flexible():
    total = 0
    print("Please enter the items you want to order. Type 'done' when finished.")
    while True:
        user_input = input("Enter item: ").strip()
        if user_input.lower() == 'done':
            break
        item = normalize_item_name(user_input)
        if item and item in menu:
            total += menu[item]
            print(f"Added {item} to your order. Current total: ${total:.2f}")
        else:
            print(f"{user_input} is not on the menu. Please choose another item.")
    tax = total * 0.07  # Assuming a 7% sales tax
    total_with_tax = total + tax
    print(f"Your total before tax is: ${total:.2f}")
    print(f"Sales tax (7%): ${tax:.2f}")
    print("---------------------")
    print(f"Your total after tax is: ${total_with_tax:.2f}")
get_order_flexible()