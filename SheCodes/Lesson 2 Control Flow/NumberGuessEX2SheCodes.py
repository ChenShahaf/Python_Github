'''
Guess Number - no cube

use will guess a random number, the computer will take the input and check if
the randomized number and the user guess are the same or not and will print out
a message saying if the use won or not.
'''
#importing randint
from random import randint
from time import sleep
#defining functions needed for this programs
def get_user_guess():
    print("Welcome to Guess Number game. ")
    print("Please enter guess number between 1 to 100: ")
    user_guess = int(input())
    print ("your guess is %d" % user_guess)
    return user_guess
def com_guess():
    user_guess = get_user_guess()
    com_guess = randint(1,100)
    #print (str(com_guess))
    #QA LINES
    if user_guess <= 100 and user_guess >= 1:
        print ("Guessing a number...")
        sleep(0.5)
        print("The result is: %d" % (com_guess))
        sleep (0.3)
        if user_guess == com_guess:
            print ("Horray! you won :)")
        else:
            print ("You lost! Better luck next time ;)")
    return None
com_guess()
