RED = '\033[31m'
BOLD = '\033[1m'
RESET = '\033[0m'

def questions():
    print("Write your guesses for these questions:")
    print("1. What animal is considered man's best friend?")
    print("2. What is the capital of France?")
    print("3. What is the largest planet in our solar system?")
    print("4. What is the largest mammal in the world?")
    print("5. What is the largest ocean in the world?")
    print(f"{RED} {BOLD}Can you tell most of these were made by AI{RESET}")
    print("")
    Answers = ["dog", "Paris", "Jupiter", "blue whale", "Pacific ocean"]
    Answers = [x.lower() for x in Answers]
    Correct_Answers = 0
    Answer_Count = len(Answers)

Answers = ["dog", "Paris", "Jupiter", "blue whale", "Pacific ocean"]
Answers = [x.lower() for x in Answers]
Correct_Answers = 0
Answer_Count = len(Answers)

questions()
print("Please write your answers in lowercase.")
Guess = [input(), input(), input(), input(), input()]

for i in range(len(Answers)):
    if Answers[i] == Guess[i]:
        Correct_Answers += 1



print(f"You got {Correct_Answers / Answer_Count * 100}% correct.")