while True:
    username = input("Enter a username: ")
    if len(username) > 12:
        print("Username must be no more than 12 characters.")
    elif ' ' in username:
        print("Username must not contain spaces.")
    elif any(char.isdigit() for char in username):
        print("Username must not contain digits.")
    else:
        print("Username is valid!")
        print(f'"Welcome to the family, {username}!"')
        break

#another way to do it:
# while True:
#     username = input("Enter a username: ")
#     if len(username) > 12:
#         print("Username must be no more than 12 characters.")
#     elif not username.isalpha():
#         print("Username must contain only letters.")
#     elif not username.find(' ') == -1:
#         print("Username must not contain spaces."),
#     else:
#         print("Username is valid!")
#         print(f'"Welcome to the family, {username}!"')
#         break