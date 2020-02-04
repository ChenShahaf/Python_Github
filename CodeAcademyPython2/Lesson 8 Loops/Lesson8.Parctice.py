# Practice 2 of 15 - IS_EVEN()
'''
IS_EVEN()
Define a function is_even that will take a number x as input.
If x is even, then return True.
Otherwise, return False.
'''
def is_even(x):
    if x%2 == 0:
        print("%d is even number" % (x))
        return True
    else:
        print("%d is not even number" %(x))
        return False
#Running examples
print("Practice 2 of 15 - IS_EVEN:")
#Checking for not even
is_even(5)
is_even(10)
# Practice 3 of 15 - IS_INT
'''
IS_INT()
An integer is just a number without a decimal part 
(for instance, -17, 0, and 42 are all integers, but 98.6 is not).
For the purpose of this lesson, 
we'll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.
This means that, for this lesson, you can't just test the input to see if it's of type int.
If the difference between a number and that same number rounded is greater than zero, 
what does that say about that particular number?

INSTRUCTIONS - Define a function is_int that takes a number x as an input.
                Have it return True if the number is an integer (as defined above) and False otherwise.
'''
def is_int(x):
    absolute = abs(x)
    rounded  = round(x)
    #if we substract the rounded number from it absolute value we will know if there is a reminder
    #according to this exercise an int is a number with a value of x.00 with no reminders
    y = absolute - rounded
    if y == 0:
        print("%f is an int" %(x))
        return True
    else:
        print("%f is not an int" %(x))
        return False
#checking Function IS_INT
print("Practice 3 of 15 - IS_INT:")
#checking a value of NOT INT
is_int(10.5)
#checling a value of INT
is_int(7)
# Practice 4 of 15 - DIGIT_SUM
'''
DIGIT_SUM()

Write a function called digit_sum that takes a positive integer n as input 
and returns the sum of all that number's digits. 
For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. 
(Assume that the number you are given will always be positive.)
'''
def digit_sum(x):
    '''
    MAIN IDEA
    STEP 1- Create a duplicate of the original input number
    STEP 2 - We need to separate the digits of the numbers using the action of num/10
    STEP 3 - add each digit into a total sum (to sum up the digits)
    '''
    #creating a duplicate number for the final print line
    dopple_num = x
    #creating the total num
    total = 0
    #iterate through the original digits of the input number - x
    while x > 0:
        #printint to see how many digits are left from the original number
        print(x)
        #summing the digits by "scraping" the remainders of the digits
        #for this example: x = 4*1 + 3*10 + 2*100 + 1*1000
        #so when we use the modolu operator we can take the digits apart one by one, by iterating through them
        #after the digit is extracted by % operator we add them with the total variable
        total += x % 10
        #in order to drop the last digit we divide by 10, and since we use the integer and not float as a defult
        #all the digits that comes after the decimal digit will be dropped out
        #1234//10 = 123.4 -> 123.4/10 = 12.34 -> 12.34/10 = 1.234 -> 1.234/10 = 0.1234
        #when x hits the value of 0.1234 as an int it considers as 0 -> the condition will become False
        # since 0  > 0 does not exist anymore
        x = x//10
    print("the sum of the digits from %d is %d" % (dopple_num , total))
    return None
#Checking the function
print("Practice 4 of 15- DIGIT_SUM:")
#checking the example case of 1234
digit_sum(1234)
#ALTERNATIVE WAY OF SOLOTION FOR PRACTICE 3 OF 15 - DIGIT_SUM
def alt_digit_sum(x):
    #when turning the number to string it will be easy to run through it as chars
    #and back to digits to sum them all up
    str_num = str(x)
    total = 0
    for char in str_num:
        total += int(char)
        #here we can see the difference, the digits are separated as digits rather than a number being
        #divded by 10 factor each time
        print(int(char))
    print("the sum of the digits from %d is %d" % (x, total))
    return None
#checking the alternative way of digit sum
print("Practice 4 of 15 - DIGIT_SUM - Alternative solotion: ")
alt_digit_sum(1234)
#Practice 5 of 15 - FACTORIAL
'''
FACTORIAL() = X! = 1*2*3*....*X-1

To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. 

For example:
factorial(4) = 4! ==  4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(0) = 1 -AS DEFAULT
'''
def factorial(x):
    #REMEMBER 0! = 1
    if x == 0:
        print("The Factorial of %d! = 1 " %(x))
    else:
        #duplicate the original num
        dupp = x
        #creating a total
        #total need to start from x, since need to duplicate x*(x-1)*(x-2)*....1
        total = dupp
        #we need to put the loop up to 1, since we are multiplying and want to avoid multply with 0 (x*0 = 0)
        while dupp > 1:
            #counting down from x down to 1, according to the formula
            dupp -= 1
            #total is being "summed" up by nultipling according to the formula
            #In this example(4!) => total = 4*(4-1)*(4-2)*(4-3) = 4*3*2*1 = 24
            total *= dupp
        #printing the total to the user
        print("the factorial of %d! = %d" %(x, total))
#checking the factorial function
print("Practice 5 of 15- FACTORIAL: ")
factorial(5)
#checking for factorial 0
factorial(0)
#Alternative way to solve Practice of Factorial
def alt_factorial(x):
    total = 1
    dupple = x
    #this way maybe more efficient since if x = 0 we return total anyway so no need for IF
    while x > 0:
        total *= x
        x -= 1
    print("the factorial of %d! = %d" %(dupple, total))
#checking the code
print("Practice 5 of 15 - FACTORIAL - Alternative Solotion: ")
#checking for 0
alt_factorial(0)
#checling for 5! = 120
alt_factorial(5)
#Practice 6 of 15 - IS_PRIME
'''
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
In other words, if you want to test if a number in a variable x is prime, 
then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, 
If there is a number between 1 and x that goes in evenly, then x is not prime.

INSTRUCTION -Define a function called is_prime that takes a number x as input.
              For each number n from 2 to x - 1, test if x is evenly divisible by n.
              If it is, return False.If none of them are, then return True.
'''
def is_prime(x):
    #prime numbers are always greater than 1, including 2
    if x > 1:
        #range will count from 2 to x-1  - WHY ONLY FROM 2 TO X-1 ??
        #using for loop and not while since we have a closed range and no need to keep running the loop all the time
        for i in range(2,x):
            #if the one of the numbers in the range can divide with no remainder, then for sure the number is not prime
            #since prime number will answer these coditions:
            #1. x /x = 1
            #2. x/1 = x
            #all other operations will result with a remainder
            if x % i == 0:
                print ("%d is not a prime number" %(x))
                #we want only want print so we need to use break
                break
        else:
            # we want only want print so we need to use break
            print("%d is a prime number" %(x))
    #for all numbers that are lower than 1, 0 or 1
    else:
        print("%d is not a prime number" %(x))
#checking the function
print("Practice 6 of 15 - IS_PRIME: ")
#checking for prime number
is_prime(3)
is_prime(1)
#checking for Non prime number
is_prime(21)
# Practice 7 of 15 - REVERSE
'''
IS_REVERSE()

INSTRUCTIONS:
1. Define a function called reverse that takes a string textand returns that string in reverse. 
            For example: reverse("abcd") should return "dcba".
            
SPECIAL NOTES: 1. You may not use reversed or [::-1] to help you with this.
               2.You may get a string containing special characters (for example, !, @, or #).
'''
def is_reverse(x):
    #creating an open string to catch each char and put it inside
    reverse = ""
    #Since we want to reach the list from its last place to the first, we need to calibarte the index to the len(x)
    running_index= len(x)
    while running_index > 0:
        #putting the char in the last index of the original array to the first index of the reverse array
        #PAY ATTENTION THIS IS HOW WE SWAP FROM LAST POSITION TO NEW POSITION IN ARRAYS
        reverse += x[running_index-1]
        #need to reduce the index in order to continue to run through the array
        running_index -= 1
    #after finishing we can print the new reverse array
    print("The reverse of %s is %s" %(x, reverse))
#checking the functions of is_reverse
print("Practice 7 of 15 - IS_REVERSE: ")
is_reverse("12345")
#Practice 8 of 15 - ANTI_VOWEL:
'''
ANTI_VOWEL()

INSTRUCTIONS: 1.Define a function called anti_vowel that takes one string, text, 
                as input and returns the text with all of the vowels removed.
                HINT - To check to see if c is a vowel, you can do: c in "aeiouAEIOU".

For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. 

SPECIAL NOTES: Make sure to remove lowercase and uppercase vowels.
'''
def anti_vowel(x):
    #sine we will loop through the original string , we want to keeo only chars that are not cowels
    #hence we will create a new string to pick up all the anti_vowels into it
    final_str = ""
    #running through the original string by each char
    for char in x:
        #it is easier to just add the anti vowels instead of deleting the vowels from the original string
        #also we always want to keep the original string untouched as much as possible
        #HENCE THE CONDITION IF THE CHAR IS NOT A VOWEL ADD IT TO THE STRING
        if char not in "aeiouAEIOU":
            #ADDING THE ANI VOWELS CHARS INTO THE FINAL STRING
            final_str += char
    print("the original string is: %s, the new string without any vowels is %s" %(x, final_str))
#checking the function
print("Practice 8 of 15 - ANTI_VOWELS: ")
anti_vowel("Hey you!")
#Practice 9 of 15 - SCRABBLE_SCORE
'''
SCRABBLE_SCORE

Scrabble is a game where players get points by spelling words.
Words are scored by adding together the point values of each individual letter 
(we'll leave out the double and triple letter and word scores for now).
To the right is a dictionary containing all of the letters in the alphabet 
with their corresponding Scrabble point values.

For example: the word "Helix" would score 15 points due to the sum of the letters: 4 + 1 + 1 + 1 + 8.

INSTRUCTIONS -  1.Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble 
                    score for that word.

SPECIAL NOTES: 1. Assume your input is only one word containing no spaces or punctuation.
               2. As mentioned, no need to worry about score multipliers!
               3. Your function should work even if the letters you get are uppercase, lowercase, or a mix.
               4. Assume that you're only given non-empty strings.
'''
def scrabble_score(word):
    # Given a score board
    score = {"a": 1,"b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
             "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
             "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
             "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
             "y": 4, "z": 10
             }
    # Printing to user the score board
    print("The score board for the Scrabble game is: ")
    for key in score:
        # Print all the values in one line
        print(key, score[key], end = " ")
    # turning the string to lower case since the score board is in lower case
    word = word.lower()
    #creating a total variable to sum up the core
    total = 0
    #passing through the chars in the given word string
    for i in word:
        #for each char in the string (word) given we need to run through the dictionary of score boars
        #and add the scores into total
        for j in score:
            if i == j:
                total += score[j]
    print(" ")
    print("the score for %s is %d" %(word, total))
#checking the function
print("Practice 9 of 15 - SCRABBLE_SCORES: ")
scrabble_score("pizza")
#Practice 10 of 15 - CENSOR
'''
CENSOR

INSTRUCTIONS - Write a function called censor that takes two strings, text and word, as input. 
              It should return the text with the word you chose replaced with asterisks. 
              For example: censor("this hack is wack hack", "hack")
              should return: "this **** is wack ****"

SPCIAL INSTRUCTIONS: Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
'''
def censor(text, word):
    #split up by using white space the sentence given in text
    words = text.split()
    #creating the result string empty to fill it slowly
    result = ''
    #choosing to censor the word with stars
    stars = '*' * len(word)
    #creating counter for the loop
    count = 0
    for i in words:
        #when we receive the requested censored word we will replace it with starts in the splited array
        if i == word:
            words[count] = stars
        count += 1
    #by using the join function we can add all the words together to a new string
    result =' '.join(words)
    #printing the result
    print("the %s is being censored with the word %s: the censored sentence is: %s" %(text, word, result))
#checking the function
print("Practice 10 of 15 - CENSOR: ")
censor("this hack is wack hack", "hack")
#Practice 11 of 15 - COUNT
'''
COUNT 

INSTRUCTIONS - Define a function called count that has two arguments called sequence and item.
                Return the number of times the item occurs in the list.
                
For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).

SPECIAL NOTES: 1.Your function should return an integer.
               2.The item you input may be an integer, string, float, or even another list!
'''
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    print("the number of the item: %d appear in the sequence: %s %d times" %(item, sequence, count))

#checking the function
print("Practice 11 of 15 - COUNT: ")
count([1, 2, 1, 1], 1)
#Practice 12 of 15 - purify
'''
PURIFY

INSTRUCTIONS - Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, 
                and returns only the even numbers in a result list.
             For example, purify([1,2,3]) should return [2].

SPECIAL NOTES- Do not directly modify the list you are given as input; instead, 
               return a new list with only the even numbers.
'''
def purify(x):
    result = []
    for i in x:
        if i % 2 == 0:
            result.append(i)
    print("the even numbers in %s list are %s" %(x, result))
#checking the function
print("Practice 12 of 15 - PURIFY: ")
purify([1,2,3,4,5,6,7,8,9,10])
#Practice 13 of 15 - PRODUCT
'''
PRODUCT

INSTRUCTIONS - Define a function called product that takes a list of integers as input 
                and returns the product of all of the elements in the list. 
                
                For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
SPECIAL NOTES - 1. Don't worry about the list being empty.
                2. Your function should return an integer.



SPECIAL NOTES- Do not directly modify the list you are given as input; instead, 
               return a new list with only the even numbers.
'''
def product(x):
    product = 1
    for i in x:
        product *= i
    print("the product of all elements in %s is : %d" %(x, product))
#checking the function
print("Practice 13 of 15 - PRODUCT: ")
product([1,2])
#Practice 14 of 15 - REMOVE_DUPLICATES
'''
INSTRUCTIONS - Write a function remove_duplicates that takes in a list 
                and removes elements of the list that are the same.

For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].

SPECIAL NOTES: 1. Don't remove every occurrence, since you need to keep a single occurrence of a number.
               2. The order in which you present your output does not matter. 
                    So returning [1, 2, 3] is the same as returning [3, 1, 2].
               3. Do not modify the list you take as input! Instead, return a new list.
               
METHOD OF SOLOTION:  1. creating a new array and insert the first value of the input array into the output array
                     2. in order to make sure the values will iterate correctly we will sort the input array
                     3. we will check for each value in the input array if it is higher (only higher NOT EQUEL TO)
                        if so, we will use append to insert the next higher value into the output array
'''
def remove_duplicates(inputlist):
        if inputlist == []:
            return []
        # Sort the input list from low to high
        inputlist = sorted(inputlist)
        # Initialize the output list, and give it the first value of the now-sorted input list
        outputlist = [inputlist[0]]
        # Go through the values of the sorted list and append to the output list
        # ...any values that are greater than the last value of the output list
        for i in inputlist:
            #only if the value of i is higher than the lst index in the ourput array we will insert it
            if i > outputlist[-1]:
                outputlist.append(i)
        print("the original array was: %s, the sorted array without any duplicates is: %s" %(inputlist, outputlist))
#checking the function
print("Practice 14 of 15 - REMOVE_DUPLICATES: ")
remove_duplicates([1,3,2,1,2,1,3])
#Practice 15 of 15 -MEDIAN
'''
MEDIAN - The median is the middle number in a sorted sequence of numbers.

INSTRUCTIONS : 1. Finding the median of [7, 12, 3, 1, 6] would first consist of sorting the sequence into 
                    [1, 3, 6, 7, 12] and then locating the middle value, which would be 6.
               2. If you are given a sequence with an even number of elements, 
                    you must average the two elements surrounding the middle.
                    
For example - the median of the sequence [7, 3, 1, 4] is 3.5, 
              since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.
You can sort the sequence using the sorted() function, like so:
'''
def median(list):
    #we will sort the array
    list.sort()
    #we will create a copy of the sorted list to work on it, while keep the original untouched
    sorted_list = []
    sorted_list = list
    #we will save the length of the array in a variable so we can check if it has an odd or even number of elements
    length = len(sorted_list)
    #we will check if the list has an odd or even number of elements
    #checking ODD NUMBER OF ELEMENTS
    if length % 2 != 0:
        median_index = length // 2
        median = sorted_list[median_index]
        #acoording to the instructions, we need to give the element in the median index of the array
        print ("The sorted array is: %s, the median value is: %d" % (sorted_list, median))
    #checking if thw array has an even number of elements
    elif length % 2 == 0:
        #we need to split the array in the middle
        #we are splitting the array in the middle
        first_half = sorted_list[:length // 2]
        second_half = sorted_list[length // 2:]
        #we will find the mean value of the 2 elements that crossing the list
        median = (first_half[-1] + second_half[0]) / 2
        print ("The sorted array is: %s, the median value is: %f" % (sorted_list, median))
#checking the function
print("Practice 15 of 15 - MEDIAN: ")
#checking for even array
median([2, 4, 5, 9])
#checking for odd array
median([2, 4, 5, 9,1,3,7])

