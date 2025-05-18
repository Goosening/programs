print("SUPER TYPER")
print("TEST YOUR SKILLS")

import random
import threading
from time import sleep

red = "\033[31m"
green = "\033[32m"
bold = "\033[1m"
reset = "\033[0m"

def main():
    def difficulty():
        print("Choose difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            print("EASY MODE")
            easy()
            return 1
        elif choice == '2':
            print("MEDIUM MODE")
            medium()
            return 2
        elif choice == '3':
            print("HARD MODE")
            hard()
            return 3
        else:
            print("Invalid choice. Defaulting to Easy mode.")
            return 1

    def easy():
        words_1 = ["cat", "dog", "fish", "bird", "apple", "banana", "grape", "orange"]
        print("You have 15 seconds to type as many words as you can.")
        print("Press ENTER to start...")
        enter_1 = input()
        if enter_1 == "":
            print("GO!")
            sleep(0.5)

            time_up = threading.Event()

            def timer():
                for i in range(10, 0, -1):
                    if time_up.is_set():
                        return
                    print(f"{i} seconds left...")
                    sleep(1)
                print("Time's up")
                time_up.set()

            timer_thread = threading.Thread(target=timer)
            timer_thread.daemon = True
            timer_thread.start()

            correct_count = 0
            for i in range(10):
                if time_up.is_set():
                    break
                word = random.choice(words_1)
                try:
                    # input with a timer check
                    player_input = input(red + bold + "TYPE THIS: " + reset + word + "\n")
                except EOFError:
                    break
                if time_up.is_set():
                    break
                if player_input == word:
                    print(green + bold + "CORRECT" + reset)
                    correct_count += 1

            # wait for timer thread to finish if still running
            time_up.set()
            timer_thread.join()
            print(f"Wow, you got {correct_count} correct")
            sleep(1)
            print("Goodbye")
            sleep(1)
            return
    
    def medium():
        words_2 = ["elephant", "giraffe", "crocodile", "hippopotamus", "kangaroo"]
        print("You have 20 seconds to type as many words as you can.")
        print("Press ENTER to start...")
        enter_2 = input()
        if enter_2 == "":
            print("GO!")
            sleep(0.5)

            time_up = threading.Event()

            def timer():
                for i in range(20, 0, -1):
                    if time_up.is_set():
                        return
                    print(f"{i} seconds left...")
                    sleep(1)
                print("Time's up")
                time_up.set()

            timer_thread = threading.Thread(target=timer)
            timer_thread.daemon = True
            timer_thread.start()

            correct_count = 0
            for i in range(5):
                if time_up.is_set():
                    break
                word = random.choice(words_2)
                try:
                    # input with a timer check
                    player_input = input(red + bold + "TYPE THIS: " + reset + word + "\n")
                except EOFError:
                    break
                if time_up.is_set():
                    break
                if player_input == word:
                    print(green + bold + "CORRECT" + reset)
                    correct_count += 1

            # wait for timer thread to finish if still running
            time_up.set()
            timer_thread.join()
            print(f"Wow, you got {correct_count} correct")
            sleep(1)
            print("Goodbye")
            sleep(1)
            return
    
    def hard():
        words_3 = ["supercalifragilisticexpialidocious", "pseudopseudohypoparathyroidism", "floccinaucinihilipilification"]
        print("You have 40 seconds to type as many words as you can.")
        print("Press ENTER to start...")
        enter_3 = input()
        if enter_3 == "":
            print("GO!")
            sleep(0.5)

            time_up = threading.Event()

            def timer():
                for i in range(40, 0, -1):
                    if time_up.is_set():
                        return
                    print(f"{i} seconds left...")
                    sleep(1)
                print("Time's up")
                time_up.set()

            timer_thread = threading.Thread(target=timer)
            timer_thread.daemon = True
            timer_thread.start()

            correct_count = 0
            for i in range(3):
                if time_up.is_set():
                    break
                word = random.choice(words_3)
                try:
                    # input with a timer check
                    player_input = input(red + bold + "TYPE THIS: " + reset + word + "\n")
                except EOFError:
                    break
                if time_up.is_set():
                    break
                if player_input == word:
                    print(green + bold + "CORRECT" + reset)
                    correct_count += 1

            # wait for timer thread to finish if still running
            time_up.set()
            timer_thread.join()
            print(f"Wow, you got {correct_count} correct")
            sleep(1)
            print("Goodbye")
            sleep(1)
            return

    difficulty()

if __name__ == "__main__":
    main()