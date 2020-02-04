import numpy as np

my_list = range(10, -11, -2)

# for i in my_list:
#  print(i)

my_list_np = np.asarray(my_list)



for i in range(len(my_list_np)):
    if my_list_np[i] < 0:
        my_list_np[i] = -1

my_list = my_list_np

#print("is: {}".format(my_list))

list_of_lists = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]


#Mat = np.asmatrix(list_of_lists)
# print(type(Mat))
# print(Mat)
# print(Mat[1,0:3])

#broad = 2
# print(broad)
#result = Mat * broad

#print(result.flatten)

#first to make things simple we will turn the lists of lists to one list

arr = []

for list in list_of_lists:
    for i in list:
        arr.append(i)
#second we will coount each element using count in new array
freq = []
for i in range(1,9):
    print("number {} appears {} times in arr".format(i, arr.count(i)))
    freq.append(arr.count(i))



#print(freq)

#print(arr)


#second option to use numpy

np_list = np.asanyarray(list_of_lists)
#other method using numpy again set an array of blanks to count occurnces
freq_np = {}
for key in freq_np:
    freq_np[key] = [i]

print(freq_np)

#for i in range(1,9):
#    freq_np[i].append(np.count_nonzero(np_list == i))

#print(freq_np)
