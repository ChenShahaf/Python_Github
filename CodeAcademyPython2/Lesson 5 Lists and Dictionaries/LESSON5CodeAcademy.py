def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
            print (total)
        return total

lotto = [4,8,15,16]
small = count_small(lotto)
print (small)
