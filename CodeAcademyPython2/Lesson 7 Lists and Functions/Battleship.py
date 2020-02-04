'''
Creating Battelship
'''
#importing randint
from random import randint
from time import sleep
board = []
# creating 5 rows of "0"
for i in range(5):
  board.append(['0'] * 5)
# printing the board as a 5*5 grid by taking each row apart
  def print_board(board_in):
    for row in range(5):
      print (" ".join(board[row]))
#since we have a 2D board (array) we need to store 2 variables for creating ships
# randomizing ships on the board - rows
def random_row(board):
    return randint(0,len(board)-1)
# randomizing ships on the board - rows
def random_col(board):
    return randint(0,len(board)-1)
ship_row = random_row(board)
ship_col = random_col(board)
for turn in range (6):
    print ("this is your %d attempt." % (turn))
    turn = turn+1
    #prompting the user to guess where the ship is on the board (row and column)
    guess_row = int(input("Please enter a guess for a row between 1 to 5: "))
    guess_col = int(input("Please enter a guess for a column between 1 to 5: "))
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
        break
    else:
        if guess_row not in range (5) or guess_col not in range (5):
            print ("Oops, that not in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
    print ("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 5:
      print ("Game over, you only get %d turns" %(turn))
      board[ship_row][ship_col] = "Y"
      print ("Y is where the ship was.")
      print_board(board)

#QA LINES
