def pythagorem(num1, num2):
    return (num1**2 + num2**2)**0.5

def euclid(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

def main():

    print("Pythagorem or Euclid?")
    selection = input("Enter your selection: ")

    if selection == "Pythagorem":
        print("Pythagorem calculator selected.")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = pythagorem(num1, num2)
        print(f"The result is: {result}")

    elif selection == "Euclid":
        print("Euclid calculator selected.")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = euclid(num1, num2)
        print(f"The result is: {result}")

def run_calculator():
        while True:
            main()
            again = input("Do you want to perform another calculation? (yes/no): ")
            if again.lower() != 'yes':
                break

if __name__ == "__main__":
    run_calculator()