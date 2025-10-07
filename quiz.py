#Lets use our list of words to create a quiz
#there will be 10 questions
#each question will have 4 possible answers
#the user will get 10 point for each correct answer
#the user will get -5 points for each wrong answer
#at the end of the quiz the user will get a score

questions = [
    {
        "1": "What is the capital of France?",
        "2": "what is the largest planet in our solar system?",
        "3": "What is the smallest prime number?",
        "4": "What is the chemical symbol for water?",
        "5": "Who wrote 'Romeo and Juliet'?",
        "6": "What is the hardest natural substance on Earth?",
        "7": "What is the largest mammal in the world?",
        "8": "What is the main ingredient in guacamole?",
        "9": "What is the currency of Japan?",
        "10": "What is the tallest mountain in the world?"
    }
]
answers = [
    {
        "1": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "2": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "3": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "4": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"],
        "5": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "6": ["A. Gold", "B. Iron", "C. Diamond", "D. Silver"],
        "7": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
        "8": ["A. Tomato", "B. Avocado", "C. Onion", "D. Pepper"],
        "9": ["A. Yen", "B. Dollar", "C. Euro", "D. Pound"],
        "10": ["A. K2", "B. Kangchenjunga", "C. Lhotse", "D. Mount Everest"]
    }
]
correct_answers = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "A",       
    "5": "B",
    "6": "C",
    "7": "B",
    "8": "B",
    "9": "A",
    "10": "D"
}
score = 0
for i in range(1, 11):
    print(questions[0][str(i)])
    for option in answers[0][str(i)]:
        print(option)
    user_answer = input("Your answer (A, B, C, or D): ").upper()
    if user_answer == correct_answers[str(i)]:
        score += 10
        print("Correct! +10 points")
    else:
        score -= 5
        print(f"Wrong! The correct answer was {correct_answers[str(i)]}. -5 points")
    print()
print(f"Your final score is: {score} out of 100")
