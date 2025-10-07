# Lets make countdown program
import time

while True:
    user_input = input("Enter a number to start countdown (seconds): ")
    if not user_input.strip():
        print("Please enter a digit to use.")
        continue
    if not user_input.isdigit():
        print("Please only use  integers.")
        continue
    n = int(user_input)
    break

if n < 0:
    print("Please enter a non-negative integer.")
    exit() 
elif n == 0:
    print("Countdown finished!")
    exit()

while n > 0:
    print(n)
    n -= 1
    time.sleep(1)
print("Countdown finished!")

