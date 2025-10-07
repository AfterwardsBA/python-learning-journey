#lets make a weight converter!
weight_type = input("Kilograms or pounds? (kg/lbs): ")
weight = float(input("Enter weight: "))
if weight_type.lower() == "kg":
    converted_weight = weight * 2.20462
    print(f"{weight} kg is {converted_weight:.2f} lbs")
elif weight_type.lower() == "lbs":
    converted_weight = weight / 2.20462
    print(f"{weight} lbs is {converted_weight:.2f} kg")
else:
    print("Invalid input! Please enter 'kg' or 'lbs'.")
# our first weight converter!
