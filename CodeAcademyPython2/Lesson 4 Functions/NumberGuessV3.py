'''
Number Guess Program

1. the Program will roll a pair of dice
2. the program will add the values of the roll
3. the program will ask the user to guess a number 
4. the program compare the result of the user vs. the program result
5. the program determine who is the winner in the game
'''
#functions needed to be imported
from random import randint
from time import sleep
#defining functions needed for this programs
def get_user_guess():
  print ("Please enter a guess: ")
  guess = int(input())
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint (1,number_of_sides)
  max_val = number_of_sides * 2
  if number_of_sides > 20 or number_of_sides < 6:
    print("you chosen invalid number of sides to the cube.")
  else:
    print ("you have chosen %d sides to the cube" % number_of_sides)
    print ("The maximum possible value is %d." % max_val) 
    guess = get_user_guess()
    if guess > max_val:
        print("Your Guess is invalid, maxium possible guess should not exceed %d." % max_val)
    else:
        print ("Rolling...")
        sleep(0.5)
        print ("First roll is %d." % first_roll)
        sleep (0.25)
        print ("Second roll is %d." % second_roll)
        sleep (0.25)
        total_roll = first_roll + second_roll
        print("The total value is: %d" % total_roll)
        print ("Reslut is...")
        sleep (0.3)
        if (guess == total_roll):
            print ("Horray! you won :)")
        else:
            print ("You lost! Better luck next time ;)")

print("Welcome to Guess Number game. ")
print("Please enter number of sides of cube,number of sides should not exceed 20, and not less then 6: ")
number_of_sides = int(input())

  
roll_dice(number_of_sides)
