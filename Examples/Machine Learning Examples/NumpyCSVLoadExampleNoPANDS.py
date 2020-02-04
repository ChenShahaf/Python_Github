
#========================================================================================
#=====              METHOD 1 TO LOAD DATA FROM A CSV FILE WITHOUT PANDAS        =========
#========================================================================================

#STEP 1 - IMPORT NUMPY
import numpy as np

#STEP 2 - CREATE AN EMPTY LIST TO STORE ALL THE ROWS OF DATA FROM THE CSV FILE
X =[]

#STEP 3 - WE WILL LOOP OVER THE CSV FILE AND STORE EACH ROW FROM THE CSV FILE TO THE EMPTY LIST (X in this example)
for line in open('C:/Users/chen/PycharmProjects/PythonProjects/NumpyUdemy/linear_regression_class/data_2d.csv'):
    #STEP 3.1 - Since the lines in the CSV file are seperated by commas,
    #           we will use split(',') to get each value from the line

    #note now row is a list contain the cells in the line list, we need to store them so data wont be lost
    row = line.split(',')
    #since the type of the file cnsidered strings we need to cast them (the values in the line) to floats
    #we will use the map function to do so
    sample = list(map(float, row))
    #now that the data is float like we want we will append it to the empty list X
    X.append(sample)

#Since X is a list we want to convert X to np.array
X =np.array(X)

#Print to check type and to see correct converation
#print(X)

#print to check shape of X
print("The shape of X is: {}".format(X.shape))