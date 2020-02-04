'''
Rock Paper Scissors Project

The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors.
Instruct the computer to randomly select either Rock, Paper, or Scissors.
Compare the user's choice and the computer's choice.
Determine a winner (the user or the computer).
Inform the user who the winner is.
'''
# importing functions needed from modules
from random import randint
from time import sleep
#creating options list
options = ["ROCK", "PAPER", "SCISSORS"]
#creating directonary for messages to user
message = {"tie": "Yawn it's a tie! :/", 
           "won": "Yay you won! :)",
            "lost": "Aww you lost! :("}

def decide_winner(user_choice, computer_choice):
    print ("You selected %s" %(user_choice))
    print ("The Computer selected %s" %(computer_choice))
    if user_choice == computer_choice:
        print (message["tie"])
    elif user_choice == options[0] and computer_choice == options[1]:
        print (message["lost"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print (message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print (message["won"])
    elif user_choice == options[1] and computer_choice == options[2]:
        print (message["lost"])
    elif user_choice == options[2] and computer_choice == options[0]:
        print (message["lost"])
    elif user_choice == options[2] and computer_choice == options [1]:
        print (message["won"])
    return None
def play_RPS():
    print ("Enter a choice Rock, Paper or Scissors: ")
    user_choice = input()
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,2)]
    decide_winner(user_choice, computer_choice)

play_RPS()            
            

  
