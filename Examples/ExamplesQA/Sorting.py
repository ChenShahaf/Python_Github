arrayA = [2,5,17,25,3,20]

#BUBBLE SORTING / SINKING SORTING

#Ascending order
"""
for j in range(0,len(arrayA)-1):
    for i in range(0,len(arrayA)-1):
        if arrayA[i] > arrayA[i+1]:
            arrayA[i], arrayA[i + 1] = arrayA[i + 1], arrayA[i]
        elif arrayA[i] < arrayA[i+1]:
          continue
"""

#Descending order
# for j in range(0,len(arrayA)-1):
#     for i in range(0,len(arrayA)-1):
#         if arrayA[i+1] > arrayA[i]:
#             arrayA[i+1], arrayA[i] = arrayA[i], arrayA[i+1]
#         elif arrayA[i] < arrayA[i+1]:
#           continue

#Mirror - create mirror
arrayB = []
for i in range(0,len(arrayA)):
    arrayB.append(arrayA[len(arrayA)-1-i])

