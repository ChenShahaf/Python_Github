#FIRST EXAMPLE TO LOOK AT A LINE CHART

#STEP 1 IMPORT MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#STEP 2 CREATE DATA POINTS FOR X AXIS
x = np.linspace(0,10, 10000)
#print(x)

#STEP 3 CREATE FOR EXAMPLE A SINE WAVE FROM THE X POINTS WE PLOTTED AS X AXIS
y = np.sin(x)

#STEP 3 PLOT THE SINE WAVE
# plt.plot(x,y)

#WE MUST USE SHOW() TO SEE THE PLOT
#plt.show()
#plt.close()

#ADDING CONFIGURATIONS FOR THE PLOT
# plt.plot(x,y)
# plt.xlabel("Time")
# plt.ylabel("Some function of time")
# plt.title("My cool chart")
#plt.show()
#plt.close()

#EXAMPLE 2 FOR PLOT
# x = np.linspace(0, 10, 200)
# y = np.cos(x)
# plt.plot(x,y)
# plt.show()
# plt.close()
#EXAMPLE 3 SCATTER
A =pd.read_csv('C:/Users/chen/PycharmProjects/PythonProjects/NumpyUdemy/linear_regression_class/data_1d.csv',
                    header=None).values
#print(type(A))
#Choosing the first col from the A matrix to be the x range
x = A[:,0]
#Choosing the second col from the A matrix to be the y range
y = A[:,1]
#Creating the scatter plot

# figure3 = plt.scatter(x,y)
# plt.plot(x,y)
# #Showing the scatter plot
# plt.show(figure3)

#trying to add a line to the scatter
x_line = np.linspace(0,100, 100)
y_line = 2*x_line + 1

# plt.scatter(x,y)
# plt.plot(x_line, y_line)
# plt.show()
# plt.close()

#HISTAGRAM
# plt.hist(x)
# plt.show()
# plt.close()

#SHOWING UNIFORM DISTRIBUTION
R = np.random.random(10000)
# plt.hist(R)
# plt.show()
# plt.close()
#SHOWING UNIFORM WITH DIFFERENTS BINS OTHER THEN THE 10 DEFAULT
# plt.hist(R, bins=20)
# plt.show()

#FOR LINEAR REGRESSION WE CHECK THE HISTAGRAM OF THE COST FUNCTION TO CHECK IF THE DATA IS NORMALLY DISTRIBUTED
y_actual = 2*x + 1
residuals = y - y_actual
# plt.show()
# plt.hist(residuals)

#PLOTING IMAGES
#store the data of train csv
df = pd.read_csv("C:/Users/chen/PycharmProjects/PythonProjects/NumpyUdemy/LargeFiles/train.csv")
#print(df.shape)
#Turn the mage to a matrix
M = df.values
#since col[0] is the label we dont need to take it in account
im = M[0, 1:]
#we got 784 pixels as a row vector, however the real picture is the size of 28X28 so we need to reshape
#print(im.shape)
#we will reshape im
im = im.reshape(28,28)
#print(im.shape)
#WE WILL PLOT THE IMAGE
#plt.imshow(im, cmap='gray')
#PLOTTING INVERSE COLORS
plt.imshow(255 - im, cmap='gray')
plt.show()