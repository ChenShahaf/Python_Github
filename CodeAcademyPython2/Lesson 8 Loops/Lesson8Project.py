#LESSON 8 PROJECT
'''
OBJECTIVE - build a basic calendar that the user will be able to interact with from the command line.
            The user should be able to choose to:
            1. View the calendar
            2. Add an event to the calendar
            3. Update an existing event
            4. Delete an existing event

SPECIAL NOTES: The program should behave in the following way:
                1. Print a welcome message to the user
                2. Prompt the user to view, add, update, or delete an event on the calendar
                3. Depending on the user's input: view, add, update, or delete an event on the calendar
                    The program should never terminate unless the user decides to exit
'''
#Importing Functions
from time import sleep, strftime
import datetime
#creating the name of the user as a CONST VARIABLE
USER_FIRST_NAME = str(input("Please enter your first name: "))
#Since a calender is associate with date and information we need to use a dictionary here
#creating the calendar - Dates = Keys, Events = Values
calendar = {}
#Creating a function that welcome the user
def welcome():
    print("Welcome " + USER_FIRST_NAME + " to your personal calendar.")
    print("Calendar is starting...")
    sleep(0.3)
    print("Today is: " + strftime("%A, %B, %d, %Y"))
    print("The current time is: " + strftime("%H:%M:%S"))
    print("What would you like to do?")
#creating the Functionality of the Calendar
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("Press: A - to add an event, U - to update and event, V - to view the calendar"
                           "D - to delete an event, X - to exit: ")
        user_choice = user_choice.upper()
        #checking what the user chose:
        if user_choice  == "V":
            if len(calendar.keys()) < 1:
                print("The calendar is empty")
            else:
                print(calendar)
        elif user_choice  == "U":
            print("i am in update")
            date = input("What is the date to update?")
            Split_date = date.split('/')
            if len(Split_date) < 3 or int(date[6:]) < int(strftime("%Y")):
                print("Invalid date, date should be in a format of MM/DD/YYYY")
                try_again = input("Try again ? Y - yes N - no: ")
                try_again.upper()
                if try_again == "Y":
                    # this will send the user to the begining of the while loop
                    continue
                elif try_again == "N":
                    start = False
            elif date not in calendar:
                print("date is not in the calendar")
                try_again = input("Try again ? Y - yes N - no: ")
                try_again.upper()
                if try_again == "Y":
                    # this will send the user to the begining of the while loop
                    continue
                elif try_again == "N":
                    start = False
            else:
                update = input("Enter the update: ")
                if update.isalpha() == False:
                    print("Event cant be a date")
                    try_again = input("Try again ? Y - yes N - no: ")
                    try_again.upper()
                    if try_again == "Y":
                        # this will send the user to the begining of the while loop
                        continue
                    elif try_again == "N":
                        start = False
                else:
                    print("Update completed.")
                    calendar[date] = update
                    print(calendar)
        elif user_choice  == "A":
            event = input("Enter an event: ")
            if event.isalpha() == False:
                print("Event cant be a date")
                try_again = input("Try again ? Y - yes N - no: ")
                try_again.upper()
                if try_again == "Y":
                    # this will send the user to the begining of the while loop
                    continue
                elif try_again == "N":
                    start = False
            elif event.isalpha() == True:
                date = input("Enter a date: (MM/DD/YYYY): ")
                #using splitting string we will check the date
                Split_date= date.split('/')
                #checking if the user entered the date correctly
                #also checking if the year is correct
                if len(Split_date) < 3 or int(date[6:]) < int(strftime("%Y")):
                    print("Invalid date, date should be in a format of MM/DD/YYYY")
                    try_again = input("Try again ? Y - yes N - no: ")
                    try_again.upper()
                    if try_again == "Y":
                        #this will send the user to the begining of the while loop
                        continue
                    elif try_again == "N":
                        start = False
                else:
                    print(calendar)
                    calendar[date] = event
                    print("the event added successfully.")
                    print(calendar)
        elif user_choice == "D":
            #if the calendar doesnt have any event, we cant delete them so we will check if there are any events at all
            event = input("What event to delete?")
            #checking if the event is indeed in the calendar
            only_letters = event.isalpha()
            if len(calendar.keys()) < 1:
                print("Calendar is empty.")
            elif only_letters == False:
                #checking the validation of the event
                print("Invalid input, event cant be a number")
                try_again = input("Try again ? Y - yes N - no: ")
                try_again.upper()
                if try_again == "Y":
                    # this will send the user to the begining of the while loop
                    continue
                elif try_again == "N":
                    start = False
            else:
                if calendar[date] == event:
                    calendar.pop(date)
                    print(calendar)
                    continue
        elif user_choice == "X":
            start = False
        #checking what if the user did not enter A/D/U/X
        else:
            print("Invalid input")
            start = False

start_calendar()