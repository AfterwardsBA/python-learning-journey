price = input("Enter the price: ")
quantity = input("Enter the quantity: ")
total = float(price) * int(quantity)
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