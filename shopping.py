# Lets combine shopping lists and user input to create a simple shopping cart application!
# The user can add items to their cart and see the total price including taxes and discounts.
# We will use concepts like lists, loops, conditionals, and user input to achieve this.
# The user can add items to their cart and see the total price including taxes and discounts.
# We will use concepts like lists, loops, conditionals, and user input to achieve this.
# This is a simple shopping cart application.

list_of_items = {
    "apple": 1.00,
    "banana": 0.50,
    "orange": 0.75,
    "grape": 2.00,
    "mango": 1.50
}
cart = []
print("Available items and their prices:")
for item, price in list_of_items.items(): 
    print(f"- {item}: ${price:.2f}")

while True:
    choice = input("Enter an item to add to your cart (or 'done' to finish): ").strip().lower()
    if choice == 'done':
        break
    elif choice in list_of_items:
        quant = input(f"How many {choice}s would you like to add? ")
        for _ in range(int(quant)):
            cart.append(choice)
        print(f"{quant} {choice}s has been added to your cart.")
    else:
        print("Item not available. Please choose from the available items.")

print("Your shopping cart contains:")
total = 0
cart_summary = {}

for item in cart:
    cart_summary[item] = cart_summary.get(item, 0) + 1

for item, quantity in cart_summary.items():
    price = list_of_items[item]
    item_total = price * quantity
    total += item_total
    print(f"- {quantity} x {item}: ${item_total:.2f}")

taxes = total * 18 / 100
print(f"Total: ${total:.2f}")
print(f"Taxes: ${taxes:.2f}")

discount = input("Do you have a discount code? (yes/no): ")
if discount.lower() == 'yes':
    per = input("Enter your discount percentage: ")
    discount_amount = (total + taxes) * float(per) / 100
    print(f"Discount amount: ${discount_amount:.2f}") 
    final_amount = (total + taxes) - discount_amount
    print(f"Final amount to pay: ${final_amount:.2f}")
else:
    final_amount = total + taxes
    print(f"Final amount to pay: ${final_amount:.2f}")

# There you have it! A simple shopping cart application that allows users to add items, see their cart summary, and calculate total costs with taxes and discounts.