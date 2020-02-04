#INTRODUCTION TO BITWISE OPERATORS

#Part 1 of 14 Just a Little BIT
def Part1():
    ''''
    Welcome to an intro level explanation of bitwise operations in Python!

    Bitwise operations might seem a little esoteric and tricky at first, but you'll get the hang of them pretty quickly.
    Bitwise operations are operations that directly manipulate bits.
    In all computers, numbers are represented with bits, a series of zeros and ones.
    In fact, pretty much everything in a computer is represented by bits. This course will introduce you to the basic bitwise operations and then show you what you can do with them.
    Bitwise operators often tend to puzzle and mystify new programmers,
    so don't worry if you are a little bit confused at first.
    To be honest, you aren't really going to see bitwise operators in everyday programming.
    However, they do pop up from time to time, and when they do, you should have a general idea of what is going on.
    '''
    # print Right shift
    print(5>>4)
    #print Left shift
    print(5<<1)
    # Print Bitwise AND
    print(8&5)
    #Print Bitwise OR
    print(9|4)
    #print Bitwise XOR
    print(12^42)
    #print Bitwise NOT
    print(~88)
    return None
#Part 2 of 14 - Lesson I0: The Base 2 Number System
def Part2():
    '''
    When we count, we usually do it in base 10. That means that each place in a number can hold one of ten values,
    0-9.
    In binary we count in base two, where each place can hold one of two values: 0 or 1.
    The counting pattern is the same as in base 10 except when you carry over to a new column,
    you have to carry over every time a place goes higher than one (as opposed to higher than 9 in base 10).

For example, the numbers one and zero are the same in base 10 and base 2.
             But in base 2, once you get to the number 2 you have to carry over the one,
             resulting in the representation "10". Adding one again results in "11" (3)
             and adding one again results in "100" (4).
            Contrary to counting in base 10,
            where each decimal place represents a power of 10,
            each place in a binary number represents a power of two (or a bit).
            The rightmost bit is the 1's bit (two to the zero power),
            the next bit is the 2's bit (two to the first), then 4, 8, 16, 32, and so on.

The binary number '1010' is 10 in base 2 because the 8's bit and the 2's bit are "on":

In Python, you can write numbers in binary format by starting the number with 0b.
 When doing so, the numbers can be operated on like any other number!
'''
    print(0b1)
    print(0b10)
    print(0b11)
    print(0b101)
    print(0b110)
    print(0b111)
    print("********")
    print(0b1 + 0b11)
    print(0b11 * 0b11)
#Part 3 of 14 - I Can Count to 1100!
def Part3():
    one = 0b01
    two = 0b10
    three = 0b11
    four = 0b100
    five = 0b101
    six = 0b110
    seven = 0b111
    eight = 0b1000
    nine = 0b1001
    ten = 0b1010
    eleven = 0b1011
    twelve = 0b1100
    thirteen = 0b1101
    fourteen = 0b1110
    fiftheen = 0b1111
    print(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fiftheen)
#Part 4 of 14 The bin() Function
def Part4():
'''
Excellent! The biggest hurdle you have to jump over in order to understand bitwise
 operators is learning how to count in base 2. Hopefully the lesson should be easier for you from here on out.
There are Python functions that can aid you with bitwise operations.
In order to print a number in its binary representation,
you can use the bin() function.
bin() takes an integer as input and returns the binary representation of that integer in a string.
(Keep in mind that after using the bin function, you can no longer operate on the value like a number.)
You can also represent numbers in base 8 and base 16 using the oct() and hex() functions.
(We won't be dealing with those here, however.)
'''



#Part3()
