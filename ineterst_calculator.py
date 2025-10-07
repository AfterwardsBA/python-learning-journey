# We will see how to create an interest calculator
# We will ask user for principal amount, rate of interest and time period
# We will calculate the interest and total amount

# principal with empty check
while True:
    principal_input = input("Enter the principal amount: ").strip()
    if not principal_input:
        print("Please enter a value!")
        continue
    try:
        principal = float(principal_input.replace(',', ''))
        if principal <= 0:
            print("Principal amount must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

# rate with empty check  
while True:
    rate_input = input("Enter the rate of interest (in %): ").strip()
    if not rate_input:
        print("Please enter a value!")
        continue
    try:
        rate = float(rate_input)
        if rate < 0 or rate > 100:
            print("Rate of interest must be between 0 and 100.")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

# time with empty check
while True:
    time_input = input("Enter the time period (in years): ").strip()
    if not time_input:
        print("Please enter a value!")
        continue
    try:
        time = float(time_input)
        if time <= 0:
            print("Time period must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

interest = (principal * rate * time) / 100
total_amount = principal + interest
print(f"Interest: {int(interest):,}")
print(f"Total amount after {int(time)} years: {int(total_amount):,}")
