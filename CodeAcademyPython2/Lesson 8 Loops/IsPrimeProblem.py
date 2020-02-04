'''
IS PRIME FUNCTION

A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
In other words, if you want to test if a number in a variable x is prime,
then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime,
If there is a number between 1 and x that goes in evenly, then x is not prime.

INSTRUCTIONS -Define a function called is_prime that takes a number x as input.
              For each number n from 2 to x - 1, test if x is evenly divisible by n.
              If it is, return False.If none of them are, then return True.
'''
'''
def is_prime(x):
    #Since all numbers under 2 are not prime numbers
    if x < 2:
        print("%d is not a prime number" %(x))
    else:
        for n in range(2, x-1):
            if x % n == 0:
                print("%d is not a prime number" %(x))
            else:
                print("%d is a prime number" %(x))
                break
#checking the function for a prime number
is_prime(4)
#checking the function for a non prime number - FOR CASE OF 3 PROGRAM DOESNT WORK
is_prime(21)

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

is_prime(3)