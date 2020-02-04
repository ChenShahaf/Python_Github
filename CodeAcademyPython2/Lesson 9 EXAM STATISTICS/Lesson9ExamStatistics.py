#LESSON 9 - EXAM STATISTICS

'''
Lesson 9 -

INSTRUCTIONS - Creating a program to compute statistics
                means that you won't have to whip out your calculator and manually crunch numbers.
                All you'll have to do is supply a new set of numbers and our program does all of the hard work.

OBJECTIVE - some practice with functions, lists, and translating mathematical formulae into programming statements.
            In order to use the scores in our program, we'll need them in a container, namely a list.

'''
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


#CREATING A FNCTION TO PRINT THE GRADES
def print_grades(grades_input):
    for i in grades_input:
        print(i, end = " ")
    print("")
#CREATING A FUNCTION THAT COMPUTES THE SUM OF THE GRADES
def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    #QA LINES
    #print(total)
    return total

#FINDING THE AVERAGE OF THE GRADES
def grades_average(grades_input):
    total = grades_sum(grades_input)
    #finding the amount of elements in the grades array
    length = len(grades_input)
    #calculating the average grade
    average = float(total/length)
    #QA LINES
    #print(average)
    return average
#COMPUTING VARIANCE
'''
VARIANCE = A very large variance means that the students' grades were all over the place,
            while a small variance (relatively close to the average) 
            means that the majority of the students had similar grades. 
'''
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    #computing variance using for loop
    for score in scores:
        variance += (average - score)**2
    variance = variance/len(scores)
    #QA LINES
    #print(variance)
    return variance
#COMPUTING STANDART DEVIATION
'''
STANDART DEVIATION = The square root of the variance. 
                      You can calculate the square root by raising the number to the one-half power.
'''
def grades_std_deviation(variance):
    return variance**0.5
#checking all functions
print(print_grades(grades))
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
variance = grades_variance(grades)

print (grades_std_deviation(variance))