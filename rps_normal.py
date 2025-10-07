#Lets make a rock paper scissors game in python
# The user will play against the computer
# The user will input their choice and the computer will randomly select a choice
# The winner will be determined based on the rules of the game
# Rock beats scissors, scissors beats paper, paper beats rock
# The game will continue until the user decides to quit
import random
import random

def get_user_choice():
    user_input = input("Enter rock(r), paper(p), scissors(s) or quit(q) to exit: ").lower()
    
    choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'q': 'quit'}
    
    if user_input in choice_map:
        return choice_map[user_input]
    elif user_input in ['rock', 'paper', 'scissors', 'quit']:
        return user_input
    else:
        print("Invalid input. Please try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock Paper Scissors!")
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
            
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

play_game()

#you can make a cheated version of this game where the computer always wins more easily than normal game but that's enough for now

    