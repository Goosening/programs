print("Welcome to the letter counter")
print("This program counts the number of letters in a given string.")
print("")

user_input = input("Please type anything here: ")
user_input = user_input.replace(" ", "") # Remove spaces
user_input = user_input.replace("\t", "") # Remove tabs
user_input = user_input.replace("\n", "") # Remove new lines
print("")

letter_count = 0
for string in user_input:
    letter_count += len(string)

print(f"The total number of letters/symbols in the given string is: {letter_count}")
print("Thank you for using the letter counter")