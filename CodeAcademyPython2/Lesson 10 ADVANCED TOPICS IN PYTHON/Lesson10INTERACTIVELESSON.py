#Learning iterating trhough dictionaries
#Practice 1 of 18 - Iterators for Dictionaries
my_dict = {"Age": "30",
           "Name": "Chen Shahaf",
            "Job": "Loser"}
print("Practice 1 of 18 - Iterators for Dictionaries")
print(my_dict.items())
#Practice 2 of 18 - keys() and values()
'''
While .items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:
The .keys() method returns a list of the dictionary's keys, and
The .values() method returns a list of the dictionary's values.
Again, these methods will not return the keys or values from the dictionary in any specific order.

You can think of a tuple as an immutable (that is, unchangeable) list. 
Tuples are surrounded by ()s and can contain any data type.

INSTRUCTIONS - 1. call to .keys() 
               2. call to .values()
               3. print both
'''
print("Practice 2 of 18 - keys() and values()")
print(my_dict.keys())
print(my_dict.values())
#Practice 3 of 18 - The 'in' Operator
'''
For iterating over lists, tuples, dictionaries, and strings, 
Python also includes a special keyword: in. You can use in very intuitively, like so:

EXAMPLE 1:
for number in range(5):
    print (number, enf =" ")
EXAMPLE 2:
    d = {"name" : "Eric",
          "age" : 26
         }
    for key in d:
        print(key, d[key], end= "")
EXAMPLE 3:
    for letter in "Eric"
        print(letter)
        
INSTRUCTION - For each key in my_dict: print out the key , 
               then a space, then the value stored by that key. 
               (You should use print a, b rather than print a + " " + b.)
'''
print("Practice 3 of 18 - The 'in' Operator")
for key in my_dict:
    print(key, my_dict[key],)
#Practice 4 of 18 - Building Lists
'''
Building Lists - if we wanted to generate a list according to some logic—for example, 
                    a list of all the even numbers from 0 to 50? - see the print syntax below
                Python's answer to this is the list comprehension. 
                List comprehensions are a powerful way to generate lists using the for/in and if keywords we've learned.
'''
print("Practice 4 of 18 - Building Lists")
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50)
#Practice 5 of 18 - List Comprehension Syntax
'''
EXAMPLE OF COMPREHENSION SYNTAX:
    new_list = [x for x in range(1, 6)]  ===>  [1, 2, 3, 4, 5]
    This will create a new_list populated by the numbers one to five. 
EXAMPLE 2:
    If you want those numbers doubled, you could use:
    doubles = [x * 2 for x in range(1, 6)] ==> [2, 4, 6, 8, 10]

INSTRUCTIONS - Use a list comprehension to build a list called even_squares in the editor.
                Your even_squares list should include the squares of the even numbers between 1 to 11. 
                Your list should start [4, 16, 36...] and go from there.
'''
print("Practice 5 of 18 - List Comprehension Syntax")
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
print(doubles_by_3)
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
print(even_squares)
#Practice 6 of 18 - Now You Try! - CUBES_BY_FOUR
'''
INSTRUCTION- 1. Use a list comprehension to create a list, cubes_by_four.
                The comprehension should consist of the cubes of the numbers 1 through 10 
             2. only if the cube is evenly divisible by four.
             3. Finally, print that list to the console.
Note that in this case, the cubed number should be evenly divisible by 4, not the original number.
'''
print("Practice 6 of 18 - CUBES_BY_FOUR")
cubes_by_four = [x**3 for x in range(1,11) if ((x**3)%4) == 0]
print(cubes_by_four)
#Practice 7 of 18 - Now You Try! - List Slicing Syntax
'''
List Slicing Syntax-  Sometimes we only want part of a Python list. 
                      List slicing allows us to access elements of a list in a concise manner. 
The syntax looks like this: [start:end:stride]
                            start describes where the slice starts (inclusive), 
                            end is where it ends (exclusive), 
                            and stride describes the space between items in the sliced list. 

For example, a stride of 2 would select every other item from the original list to place in the sliced list.

'''
print("Practice 7 of 18 - List Slicing Syntax")
listA = [i**2 for i in range(1, 11)]
print(listA)
#slicing through the number : 3, 5 , 7, 9 since we start at 1 -> 11 with steps of 2, so that gives us 3,5,7,9
#Practice 8 of 18 - Now You Try! - Omitting Indices
'''
If you don't pass a particular index to the list slice, Python will pick a default.
to_five = ["A", "B", "C", "D", "E"]
print (to_five[3:]) ==> prints ["D", "E"]

1. The default starting index is 0.
2. The default ending index is the end of the list.
3. The default stride is 1.
'''
print("Practice 8 of 18 - Omitting Indices")
my_lst = list(range(1, 11))
#EXAPLAIN HOW TO OVER COME THIS PRINT
print (my_lst)
#we will print eaach odd element in the list
print(my_lst[::2])
#Practice 9 of 18 - Reversing a List
print(my_lst[::-1])
#Practice 10 of 18 - Stride Length
#Stride Length -  A positive stride length traverses the list from left to right,
#                  and a negative one traverses the list from right to left.
#                  Further, a stride length of 1 traverses the list "by ones,"
#                  a stride length of 2 traverses the list "by twos," and so on.

print("Practice 10 of 18 - Stride Length")
to_one_hundred = list(range(101))
backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)
# 11 of 18 -Practice Makes Perfect
'''
INSTRUCTIONS - 1. Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
               2. Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). 
                  Use list slicing for this one instead of a list comprehension.
               3. Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, 
                  inclusive.
'''
print("Practice 11 of 18 - Practice Makes Perfect")
listB = list(range(1,22))
odds = listB[::2]
middle_third = listB[7:14]
print(odds)
print(middle_third)
#12 of 18 -Anonymous Functions
'''
One of the more powerful aspects of Python is that it allows for a style of programming called functional programming,
 which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!
 Check out the code at the right. See the lambda bit? Typing
 
 lambda x: x%3 == 0
 
 Only we don't need to actually give the function a name; it does its work and returns a value without one. 
 That's why the function the lambda creates is an anonymous function.
 When we pass the lambda to filter, filter uses the lambda to determine what to filter, 
 and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
'''
print("Practice 12 of 18 - Anonymous Functions")
my_listC = list(range(1,16))
print(my_listC)
print (list(filter(lambda x: x%3 == 0, my_listC)))
#13 of 18 -Anonymous Functions
print("Practice 13 of 18 - Lambda Syntax")
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == "Python", languages)))
#14 of 18 - Try It! - Lambda Syntax
print("Practice 14 of 18 - Try it! - Lambda Syntax")
listD = list(range(1,11))
squares = [x**2 for x in range(1, 11)]
print(list(squares))
print(list(filter(lambda x: x >= 30 and x <= 70, squares)))
#15 of 18 - Iterating Over Dictionaries
'''
Call the appropriate method on movies such that it will print out all the items (hint, hint) 
in the dictionary—that is, each key and each value.

print("Practice 15 of 18 - Iterating on dictionary with no loop")
'''
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print(movies.items())
#16 of 18 - Comprehending Comprehensions
'''
SYNTAX FOR ANOTHER  COMPREHENSIONS: squares = [x ** 2 for x in range(5)]

print("Practice 16 of 18 - Comprehending Comprehensions")
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print (threes_and_fives)
#17 of 18 - List Slicing

str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]

You can think of a Python string as a list of characters.
'''
print("Practice 17 of 18 - List Slicing")
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print (message)
#18 of 18 - Lambda Expressions
print("Practice 18 of 18 - Lambda Expressions")
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = (list(filter(lambda x: x != "X", garbled,)))
spaces_words = "".join(message)
spaces_words.split()
print(spaces_words)

