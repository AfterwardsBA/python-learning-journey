#Lets make a rock paper scissors game in python but with a funny twist
# The user will play against the computer and win 5 times in a row but in the last round the computer will cheat and win with a gun!

player = input("Enter your name: ")
print(f"Welcome {player} to Rock, Paper, Scissors, Gun game!")
print("You will play against the computer.")
print("The rules are simple:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print("Gun beats Rock, Paper, and Scissors")

print("You will play 5 rounds and win all of them.")
print('But there is a twist in the last round! Await it to find out!')
print("Let's start the game!")

score = 0
rounds_to_play = 5

for round in range(1, rounds_to_play + 1):
    user_choice = input(f"Round {round}: Enter Rock(r), Paper(p), or Scissors(s): ").lower()
    
    #Thee short form control
    choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    if user_choice in choice_map:
        user_choice = choice_map[user_choice]
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue
    
    # Computer will always lose
    if user_choice == 'rock':
        computer_choice = 'scissors'
    elif user_choice == 'paper':
        computer_choice = 'rock'
    else:  # scissors
        computer_choice = 'paper'
    
    print(f"Computer chose: {computer_choice.title()}")
    print("You won this round!")
    score += 20
    print(f"Your current score is: {score}")

# Last round twist
if round == rounds_to_play:
    double = input("Do you want to double your points in the next round? (yes/no): ").lower()
    
    if double == 'yes':
        print("\n--- FINAL ROUND ---")
        last_choice = input("Enter Rock(r), Paper(p), or Scissors(s): ").lower()
        
        # The short form control
        if last_choice in choice_map:
            last_choice = choice_map[last_choice]
        
        print(f"You chose: {last_choice.title()}")
        print("Computer chose: GUN 🔫")
        print("Computer wins this round!")
        print(f"Your final score is: 0! You lost all your points to the computer's gun!")
        print("Better luck next time!")
    else:
        print("\nComputer refuses to accept defeat and pulls out a GUN! 🔫")
        print("Computer chose: GUN")
        print("Computer wins this round!")
        print(f"Your final score is: 0! You lost all your points to the computer's gun!")
        print("Better luck next time!")
print("Thanks for playing!")


#There you have it, a funny twist on the classic game!