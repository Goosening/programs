print("Welcome to the Word Guesser Game")
print("You have 6 attempts to guess the word.")

import random

words = ["python", "java", "kotlin", "javascript", "html", "css", "ruby", "swift"]

word = random.choice(words)
guessed_letters = []
attempts = 6
correct_guesses = ["_"] * len(word)

def display_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    global attempts  # To modify the global attempts variable
    while attempts > 0 and "_" in correct_guesses:
        print("\nCurrent word: ", display_word())
        print("Attempts left: ", attempts)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for index, letter in enumerate(word):
                if letter == guess:
                    correct_guesses[index] = guess
        else:
            print("Wrong guess.")
            attempts -= 1

    if "_" not in correct_guesses:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nSorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    main()