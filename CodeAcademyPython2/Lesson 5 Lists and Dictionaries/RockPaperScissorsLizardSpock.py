'''
Rock Paper Scissors Project

The program should do the following:

Prompt the user to select either Rock, Paper, Scissors, Lizard or Spock.
Instruct the computer to randomly select either Rock, Paper, Scissors, Lizard or Spock.
Compare the user's choice and the computer's choice.
Determine a winner (the user or the computer).
Inform the user who the winner is.

'''
# importing functions needed from modules
from random import randint
from time import sleep
#creating options list
options = ["ROCK", "PAPER", "SCISSORS","LIZARD", "SPOCK"]
#creating directonary for messages to user
message = {"tie": "Damn it's a tie o_O", 
           "won_rock_paper": "paper wrap Rock, you won ^.^",
           "won_rock_scissors": "Rock crushes scissors, you won ^_^",
           "won_rock_Lizard": "Rock crushes Lizard, you won :)",
           "won_rock_spock": "Spock Vaporizes Rock, you won ;)",
           "won_scissors_paper": "Scissors cuts Paper, you won ^.^",
           "won_paper_spock": "Paper disproves Spock, you won $_$",
           "won_lizard_spock": "Lizard poisions Spock, you won XD",
           "won_lizard_paper": "Lizard eats Paper, you won :)",
           "won_lizard_scissors": "Scissors decapitates Lizard, you won x_X",
           "lost_paper_rock": "Paper wrap Rock, you lost x_X",
           "lost_paper_scissors": "Scissors cuts Paper, you lost!",
           "lost_scissors_rock": "Rock crushes scissors, you lost :(",
           "lost_lizard_rock": "Rock crushes Lizard, you lost o_O",
           "lost_rock_spock": "Spock Vaporizes Rock, you lost x_X",
           "lost_lizard_spock": "Lizard poisions Spock, you lost :P",
           "lost_lizard_scissors": "Scissors decapitates Lizard, you lost x_X",
           "lost_lizard_paper": "Lizard eats Paper, you lost o_O",
           "lost_spock_scissors": "Spock smashes Scissors, you lost x.X"
           }
def decide_winner(user_choice, computer_choice):
    print ("You selected %s" %(user_choice))
    sleep (0.3)
    print ("The Computer selected %s" %(computer_choice))
    sleep (0.3)
    if user_choice == computer_choice:
        print (message["tie"])
    elif user_choice == options[0] and computer_choice == options[1]:
        print (message["lost_paper_rock"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print (message["won_rock_scissors"])
    elif user_choice == options[0] and computer_choice == options[3]:
        print (message["won_rock_Lizard"])
    elif user_choice == options[0] and computer_choice == options[4]:
        print (message["lost_rock_spock"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print (message["won_rock_paper"])
    elif user_choice == options[1] and computer_choice == options[2]:
        print (message["lost_paper_scissors"])
    elif user_choice == options[1] and computer_choice == options[3]:
        print (message["lost_lizard_paper"])    
    elif user_choice == options[1] and computer_choice == options[4]:
        print (message["won_paper_spock"])
    elif user_choice == options[2] and computer_choice == options[0]:
        print (message["lost_scissors_rock"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print (message["won_scissors_paper"])
    elif user_choice == options[2] and computer_choice == options[3]:
        print (message["won_lizard_scissors"])
    elif user_choice == options[2] and computer_choice == options[4]:
        print (message["lost_spock_scissors"])
    elif user_choice == options[3] and computer_choice == options[0]:
        print (message["lost_lizard_rock"])
    elif user_choice == options[3] and computer_choice == options[1]:
        print (message["won_lizard_paper"])
    elif user_choice == options[3] and computer_choice == options[2]:
        print (message["lost_lizard_scissors"])
    elif user_choice == options[3] and computer_choice == options[4]:
        print (message["won_lizard_spock"])
    elif user_choice == options[4] and computer_choice == options[0]:
        print (message["lost_lizard_rock"])
    elif user_choice == options[4] and computer_choice == options[1]:
        print (message["won_lizard_paper"])
    elif user_choice == options[4] and computer_choice == options[2]:
        print (message["lost_lizard_scissors"])
    elif user_choice == options[4] and computer_choice == options[3]:
        print (message["lost_lizard_spock"])
    return None
def play_RPS():
    print ("Enter a choice Rock, Paper, Scissors, Lizard or Spock: ")
    user_choice = input()
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,4)]
    decide_winner(user_choice, computer_choice)
    return None
play_RPS()            
            

  
