from time import sleep, strftime

# Constant variable with the user's first name
USER_FNAME = "Vy"

# Calendar = dictionary (event + date as a pair)
calendar = {}


# Welcome message
def welcome():
    print("Hello " + USER_FNAME + " !")
    print("The Python Command Line Calendar is opening...")
    sleep(1)
    print("Today is " + strftime("%A %B %d %Y"))
    print(strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do? ")


# Printing the calendar in the appropriate format
def print_calendar():
    if len(calendar.keys()) < 1:
        print("There is no event in the calendar for now.")
        return
    else:
        print("\n")
        print("There are {} event(s) in the calendar.".format(len(calendar)))
        for date in calendar:
            print(date, calendar[date])
        print("\n")


# Calendar functions
def start_calendar():
    welcome()
    start = True

    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ").upper()

        # VIEW FUNCTION
        if user_choice == "V":
            print_calendar()

        # ADD FUNCTION
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYY): ")
            if len(date) > 10 or int(date[6:len(date)]) < int(strftime("%Y")):
                print("Invalid date.")
                try_again = input("Try again ? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print("Successfully added.")
                print_calendar()

        # UPDATE FUNCTION
        elif user_choice == "U":
            if len(calendar.keys()) < 1:
                print("There is nothing to update.")
            else:
                date = input("What date? (MM/DD/YYYY) ")
                update = input("Enter the update: ")
                calendar[date] = update
                print("Successfully updated.")
                print_calendar()

        # DELETE FUNCTION
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print("There is no event in the calendar to delete.")
            else:
                event = input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print("Successfully deleted.")
                        print_calendar()
                    else:
                        print("Incorrect event.")

        # EXIT FUNCTION
        elif user_choice == "X":
            start = False

        # OTHER
        else:
            print("Invalid command.")
            start = False
