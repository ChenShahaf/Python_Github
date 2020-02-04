
def sum_double(a,b):
    sum = a+b
    if a == b:
        sum = sum*2
    return sum

print ("Please choose variables a and b: ")
print ("Please note, if a = b, the result will be a*4")
a = input()
b = input()
sum = sum_double(a,b)
print ("The result is %d") % sum