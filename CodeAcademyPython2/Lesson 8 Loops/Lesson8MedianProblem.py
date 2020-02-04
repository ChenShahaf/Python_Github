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
median([2, 4, 5, 9])
