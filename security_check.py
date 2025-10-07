# Lets try to do a security check!
# We will have credit card number, password and email
# We will check if the credit card number is valid (16 digits)
# We will check if the password is strong (at least 8 characters, contains at least one uppercase letter, one lowercase letter, one digit and one special character)
# We will check if the email is valid (contains @ and .)
import re
while True:
    credit_card = input("Enter your credit card number (16 digits): ")
    if len(credit_card) != 16 or not credit_card.isdigit():
        print("Invalid credit card number. It must be 16 digits.")
        continue
    elif not re.match(r"^[0-9]{16}$", credit_card):
        print("Invalid credit card number format.")
        continue
    elif credit_card.startswith('0'):
        print("Credit card number cannot start with 0.")
        continue
    elif credit_card.find(' ') != -1:
        print("Don't use breaks in your credit card number.")
        continue

    password = input("Enter your password: ")
    if (len(password) < 8 or
            not re.search(r"[A-Z]", password) or
            not re.search(r"[a-z]", password) or
            not re.search(r"[0-9]", password) or
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        print("Weak password. It must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        continue

    email = input("Enter your email: ")
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Invalid email address. It must contain '@' and a domain (e.g., '.com').")
    elif email.find(' ') != -1:
        print("Email must not contain spaces.")
        continue
    break


print("All inputs are valid!")
print(f"Credit Card: {'*' * 12 + credit_card[-4:]}")  # Mask all but last 4 digits
print(f"Password: {'*' * len(password)}")  # Mask the password
print(f"Email: {email}")
print("Information saved and secured.")
print("Welcome aboard!")