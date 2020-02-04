'''
Lesson 8 - Loops in CodeAcademy
link - https://www.codecademy.com/courses/learn-python/lessons/loops/
            exercises/create-your-own?action=resume_content_item
'''
#1 of 19 - While you're here
'''
The while loop is similar to an if statement: it executes the code inside of it if some condition is true.
THE DIFFERENCE is that the WHILE LOOP WILL CONTINUE to execute AS LONG THE CONDITION IS TRUE. 
In other words, instead of executing if something is true, it executes while that thing is true.

SYNTAX EXAMPLE
loop_condition = True

while loop_condition:
  print "I am a loop"
  
INSTRUCTION: Change the loop so that it counts from 0 up to 9 (inclusive).
Be careful not to alter or remove the count += 1 statement. 
If your program has no way to increase count, 
your loop could go on forever and become an infinite loop which could crash your computer/browser!
'''
#creating a counter to run trough the loop
print ("Part 1 of 18")
count = 0
while count <= 9:
    print("I am a loop")
    count += 1
#2 of 19 - Condition
'''
The condition is the expression that decides whether the loop is going to continue being executed or not. 
There are 5 steps to this program:

EXAMPLE
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False

1.The loop_condition variable is set to True
2.The while loop checks to see if loop_condition is True. It is, so the loop is entered.
3.The print statement is executed.
4.The variable loop_condition is set to False.
5.The while loop again checks to see if loop_condition is True. 
6. since now the condition does not apply - the loop is not executed a second time.
'''
print("Part 2 of 19")
loop_condition = True

while loop_condition:
  print ("I am a loop")
  loop_condition = False
# 3 of 19 - While you're at it
'''
Inside a while loop, you can do anything you could do elsewhere, 
including arithmetic operations.

INSTRUCTION - Create a while loop that prints out all the numbers from 1 to 10 squared 
(1, 4, 9, 16, ... , 100), each on their own line, so that our while loop goes from 1 to 10 inclusive.
Inside the loop, print the value of num squared. The syntax for squaring a number is num ** 2.
Increment num.
'''
print("Part 3 of 19")
num = 1
while num <= 10:
    print(num**2)
    #num is a counter in this loop hence it needs to be incremented in 1
    # to keep the loop alive
    num += 1
# 4 of 19 - Simple errors
'''
A common application of a while loop is to check user input to see if it is valid. 
For example, if you ask the user to enter y or n and they instead enter 7, 
then you should re-prompt them for input.

INSTRUCTION - Fill in the loop condition so the user will be prompted for a choice over and over 
               while choice does not equal 'y' and choice does not equal 'n'.
'''
print("Part 4 of 19")
choice = input("Enjoying this course so far? (y/n)")
#we need to put an AND here since we want only to aliminate chars that are not Y or N
# puting an OR in this loop will result in an infinite loop since Y or N will result in TRUE == LOOP WONT STOP
while choice != "y" and choice != "n":
    choice = input("Sorry wrong char, please try again (y/n): ")

#5 of 19 -Infinite loops
'''
An infinite loop is a loop that never exits. This can happen for a few reasons:
The loop condition cannot possibly be false (e.g. while 1 != 2)
The logic of the loop prevents the loop condition from becoming false.

INSTRUCTION - The loop in the editor has two problems: it's missing a colon (a syntax error)
                and count is never incremented (logical error). The latter will result in an infinite loop, 
                so be sure to fix both before running!
  
  LOOP IN EDITOR:              
count = 0

while count < 10 # Add a colon
  print count
  # Increment count
'''
print("Part 5 of 19")
#CORRECT CODE
count = 0
while count < 10:
    print(count)
    count += 1

#6 of 19 - Break
'''
1. The break is a one-line statement that means "exit the current loop."
2. An alternate way to make our counting loop exit and stop executing is with the break statement.
HOW BREAK WORKS:
1. First, create a while with a condition that is always true. The simplest way is shown.
2. Using an if statement, you define the stopping condition. Inside the if, you write break, meaning "exit the loop."

THE DIFFERENCE here is that this loop is guaranteed to run at least once.
count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break
'''
print("Part 6 of 19")
count = 0
while True:
  print(count)
  count += 1
  if count >= 10:
    break
#7 of 19 - While / else
'''
Something completely different about Python is the while/else construction. 
while/else is similar to if/else, but there is a DIFFERENCE: 
1. the else block will execute anytime the loop condition is evaluated to False. 
    This means that it will execute if the loop is never entered or if the loop exits normally. 
2. If the loop exits as the result of a break, the else will not be executed.

In this example, the loop will break if a 5 is generated, and the else will not execute. 
Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
'''
print("Part 7 of 19")
import random
print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")
#putting a counter to promote the loop
count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")

#8 of 19 - Your own while / else
'''
Now you should be able to make a game similar to the one in the last exercise. 
The code from the last exercise is below:

count = 0
while count < 3:
  num  = random.randint(1,6)
  print(num)
  if num == 5:
    print("Sorry you lose")
    break
count += 1
   else:
   print("You win!")
in this exercise, allow the user to guess what the number is 3 times.
guess = int(input("Your guess: "))

INSTRUCTION - 
Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
Ask the user for their guess, just like the second example above.
If they guess correctly, print "You win!" and break.
Decrement guesses_left by one.
Use an else: case after your while loop to print "You lose.".
'''
print("Part 8 of 19")
#importing random
from random import randint
ran_num = randint(1,10)
#counting guessing possiblities from 3 down to zero, creating a counter
guesses_left = 3
while guesses_left> 0:
    #catching the user guess
    user_guess = int(input("Please enter your guess of number between 1 and 10: "))
    #comparing user guess to the computer guess
    if user_guess == ran_num:
        print("You win!")
        #since the game is ended - we need to break and not complete the loop
        break
    #reducing the number of attempts inside the loop out of the if, since otherwise the while will become infinite
    guesses_left -= 1
    print("you left with %d attemps" %(guesses_left))
else:
    print("You Lose, computer guess was %d" %(ran_num))
# 9 of 19 - For your health
'''
An alternative way to loop is the for loop. 
The syntax is as shown in the code editor. 
This example means "for each number i in the range 0 - 9, print i".

THIS IS A WAY TO COUNT THROUGH INDEXES IN A LOOP

'''
print("Part 9 of 19")
print("Counting...")
#in range function the range is counted from 0 to n-1
for i in range(10):
    print(i)
# 10 of 19 - For your hobbies
'''
This kind of loop is useful when you want to do something a certain number of times, 
such as append something to the end of a list.

SYNTAX FOR LOOP FOR DOING SOMETHING REPETITIVE
'''
print("Part 10 of 19")
#we will catch 3 hobbies and store it inside a list
#STEP 1  - CREATE EMPTY LIST
hobbies = []
#STEP 2 - USING FOR LOOP TO CATCH THE VALUES TO INSERT TO THE LIST
#CHOSSING THE RANGE FUNCTION TO DECIDE HOW MANY SLOTS WE WILL HAVE IN OUR LIST
for i in range(3):
    hobby = input("Please enter a hobby: ")
    #STROGING THE VALUE (HOBBY) AND INSERT IT TO THE ARRAY USING APPEND FUNCTION
    hobbies.append(str(hobby))
#PRINTING THE ARRAY
#NOTE -WHEN PRINTING A LIST OF STRINGS USE %S
print("The Hobbies are %s" %(hobbies))
#11 of 19 - For your strings
'''
Using a for loop, you can print out each individual character in a string.
The example in the editor is almost plain English: "for each character c in thing, print c".
'''
print("Part 11 of 19")
list = "SPAM"
print(list)
print("now we will print the list by each char in the list.")
for char in list:
    print(char)

# 12 of 19 - For your A
'''
String manipulation is useful in for loops if you want to modify some content in a string.

EXAMPLE- 
word = "marble"
for char in word:
    print (char, end= <separator>) 
the , after char means that the print will look like: m a r b l e - meaning , keep the printing on the same line
'''
print("12 of 19")
phrase = "A bird in the hand..."
for char in phrase:
    if char == "a" or char == "A":
        print("X", end= " ")
    else:
        print(char, end= " ")
print
print(" ")
# 13 of 19 - For your lists
'''
Perhaps the most useful (and most common) use of for loops is to go through a list.
On each iteration, the variable num will be the next value in the list. 
So, the first time through, it will be 7, 
the second time it will be 9, then 12, 54, 99, 
and then the loop will exit when there are no more values in the list.
'''
print("13 of 19")
numbers = [7, 9, 12, 54, 99]
print("This list contains: ")
for i in numbers:
    print(i, end= " ")
print(" ")

#14 of 19 - Looping over a dictionary
'''
You may be wondering how looping over a dictionary would work. Would you get the key or the value?
The short answer is: you get the key which you can use to get the value.

dic = {'x': 9, 'y': 10, 'z': 20}
#STEP 1 - LOOPING THROUGH THE KEYS IN THE DICTIONARY
<The loop iterate through the dictionary, each time storing the key in key which is in the for loop.>
for key in dic:
    #CHECKING IF THE VALUE OF THE KEY IS CREATING TRUE ARGUMENT FOR THE IF STATEMENT
    if d[key] == 10:
    #In this example we only have one value with 10, so the print statement will appear once.
        print("This dictionary has a value of 10.")
'''
print("14 of 19")
dict = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in dict:
    #Print all the values in one line
    print(key, dict[key], end= " ")
    #Print the values in different lines  = print(key, dict[key])
print(" ")

# 15 of 19 - Counting as you go
'''
A weakness of using this for-each style of iteration is that you don't know the index of the thing you're looking at. 
Generally this isn't an issue, but at times it is useful to know how far into the list you are.
Thankfully the built-in enumerate function helps with this.
enumerate works by supplying a corresponding index to each element in the list that you pass it. 
Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. 
It's very similar to using a normal for loop with a list, 
except this gives us an easy way to count how many items we've seen so far.
'''
print("15 of 19")
choices = ['pizza', 'pasta', 'salad', 'nachos']
print("your choices are: ")
# The loop will iterate and print firstly the index of the item in the list and then the item it is associated with
#WE CHOOSE index+1 so the user don't see 0 to n-1 but rather 1 to n
for index, item in enumerate(choices):
    #Printing in one line the index and its item in the list
    print(index+1, item, end= " ")
print(" ")
#16 of 19 - Multiple lists
'''
It's also common to need to iterate over two lists at once. 
This is where the built-in zip function comes in handy.
zip will create pairs of elements when passed two lists, 
and will stop at the end of the shorter list.
zip can handle three or more lists as well!
'''
print("16 of 19")
listA =[3, 9, 17, 15, 19]
listB =[2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for i, j in zip(listA, listB):
    #printing in each list the larger value of the two
    print(max(i, j), end= " ")
    #NOTICE - the print doesnt go over 30 since list B is bigger so no more comparsion
print(" ")

#17 of 19 - FOR/Else
'''
Just like with while, for loops may have an else associated with them.
In this case, the else statement is executed after the for, 
but only if the for ends normally—that is, not with a break. 
This code will break when it hits 'tomato', so the else block won't be executed.
'''
print("17 of 19")
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print("You have...")
for i in fruits:
    if i == 'tomato':
        print("A tomato is not a fruit.")
        break
    print("A %s, " %(i), end= " \n")
else:
    print('A fine selection of fruits!')

#18 of 19 - Change it up
'''
As mentioned, the else block won't run in this case, 
since break executes when it hits 'tomato'.

INSTRUCTIONS - Modify the code in the editor such that 
                the for loop's else statement is executed.
'''
print("18 of 19")
fruits = ['banana', 'apple', 'orange', 'pear', 'grape']
print("You have...")
for i in fruits:
    if i == 'tomato':
        print("A tomato is not a fruit.")
        break
    print("A %s, " %(i), end= " ")
else:
    print('A fine selection of fruits!')
# 19 of 19 - Create your own
'''
instruction - Build your for/else statement in the editor.
 Execution of the else branch is optional, 
 but your code should print a string of your choice to the editor regardless.
 
 INSTRUCTION - change the contents of fruits OR the contents of the for statement 
                such that the loop doesn't break on "tomato".
'''
print("Part 19 of 19")
#creating an array to run through it
array = [0,1,2,3,4,5,6,7,8,9,10]
#running over the array
for i in array:
    print(i, end= " ")
else:
    print(" ")
    print("End of Array")
