#lets make a list of items and a then a shopping cart!

items = ["apple", "banana", "orange", "grape", "mango"]
cart = []
print("Available items:") 
for item in items:
    print(f"- {item}") #print available items
while True: #start an infinite loop to keep asking for items
    choice = input("Enter an item to add to your cart (or 'done' to finish): ").strip().lower() #get user input
    if choice == 'done':  #you need thisl to exit the loop
        break
    elif choice in items: #check if item is in the list
        cart.append(choice)
        print(f"{choice} has been added to your cart.") #confirm addition
    else:  
        print("Item not available. Please choose from the available items.") #handle invalid input
print("Your shopping cart contains:") #print cart contents
for item in cart:
    print(f"- {item}") #list items in cart

