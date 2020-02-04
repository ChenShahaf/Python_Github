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
def user_choice(user_choice):
    #TODO - CREATE FUNCS FOR A,D,U,V,X
    user_choice = user_choice.upper()
    if user_choice == "A":
        ADD()
    elif user_choice == "U":
        UPDATE()
    elif user_choice == "D":
        DEL_EVN()
    elif user_choice == "V":
        VIEW()
    #TODO - ADD EXIT SUBROUTINE
    elif user_choice == "X":






def welcome():
    USER_FIRST_NAME = str(input("Please enter your first name: "))
    print("Welcome " + USER_FIRST_NAME + " to your personal calendar.")
    print("Calendar is starting...")
    sleep(0.3)
    print("Today is: " + strftime("%A, %B, %d, %Y"))
    print("The current time is: " + strftime("%H:%M:%S"))
    print("What would you like to do?")
