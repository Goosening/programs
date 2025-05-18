def main():
    print("Welcome to the Time Converter.")
    print("")
    time_input = input("Please enter the time you wish to convert: ")
    time_input = time_input.split(":")

    if len(time_input) == 2:
        time_input.append("00")
    elif len(time_input) == 1:
        time_input.append("00")
        time_input.append("00")
    
    if len(time_input) != 3:
        print("Invalid time format. Please enter time in HH:MM:SS format.")
        return
    
    hours = int(time_input[0])
    minutes = int(time_input[1])
    seconds = int(time_input[2])

    print("Time in seconds: ", int((hours * 3600) + (minutes * 60) + seconds))
    print("Time in minutes: ", int((hours * 60) + minutes + (seconds / 60)))
    print("Time in hours: ", int(hours + (minutes / 60) + (seconds / 3600)))

    print("")
    
    if hours > 12:
        print("Time in 12-hour format: ", f"{hours - 12}:{minutes} PM")
    elif hours == 12:
        print("Time in 12-hour format: ", f"{hours}:{minutes} PM")
    else:
        print("Time in 12-hour format: ", f"{hours}:{minutes} AM")
    
    def validate_time(hours, minutes, seconds):
        if hours >= 24 or minutes >= 60 or seconds >= 60:
            print("Invalid time input. Hours must be less than 24, and minutes/seconds must be less than 60.")
            return False
        return True
    
    validate_time(hours, minutes, seconds)
    print("")

    print("Would you like to convert another time? (y/n)")
    while True:
        choice = input("Enter your choice: ")
        if choice.lower() == 'y':
            print("")
            main()
        elif choice.lower() == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
    

if main() == "__main__":
    main()