#Home work 3, if lecture

def check(a,b,c):
    num1 = int(a)
    num2 = int(b)
    num3 = int(c)
    if num1==num2 or num1==num3:
        return True
    elif num1!= num2 and num1!=num3 and num2!=num3:
        return False

print(check(5,'5',6))
