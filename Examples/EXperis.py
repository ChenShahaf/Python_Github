width = 7
length = 2
squers = []
while width > 0 and length > 0:
    if width > length:
        squers.append(length)
        width -= length
    else:
        squers.append(width)
        length -= width

#print(squers)

sig = [1,1]
n = 10
emp_xbonacci = sig.copy() #[1,1,2, 3]
#print(emp_xbonacci)
for i in range(len(sig),n):
    sumFib = sum(emp_xbonacci[-len(sig):])
    emp_xbonacci.append(FibSum)




