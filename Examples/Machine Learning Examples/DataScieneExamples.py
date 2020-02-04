import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
#Show a linear line
#plt.plot(year, pop)
#We will use scatter plot to show the result - only dots ike scatter XY with no line between the dots
#first argument = X-axis, second argument = Y-axis
plt.scatter(year,pop)
plt.plot(year,pop)
#Rescale X axes to be in Log on base 10
#plt.xscale('log')
#plt.show()