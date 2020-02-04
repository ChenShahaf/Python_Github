import numpy as np
from numpy import matlib

import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library


a = np.arange(4.0)
b = a*23.4
c = b/(a+1)
c += 10
#print(c)

#arr arguments are int's
arr = np.arange(100, 200)
#if we want the arange nums will be float we need dtype.float
#in numpy the casting will be as ..

#selects the nums in the indexes in our array
select = [5, 25, 50, 75, -5]
#print(arr[select])

arr = np.arange(10, 20)
#Logical indexing
#for each of the numberrs in the array we check if the number in the array is divded by 3
#the result is True or False, 10= False, 11=False, 12=True(since it is divided by 3)
div_by_3 = arr%3 == 0
#print(div_by_3)
#since div_by_3 only received the numbers which divided by 3 we can see that they are 12,15 and 18
#print(arr[div_by_3])
#reshaping the long list to a matrix of 2X5
arr = np.arange(10,20).reshape(2,5)
#print(arr)

#Array Methods
#print(arr)
arr.sum()
arr.std()
arr.max()
arr.min()
div_by_3.all()
#are all the numbers in the array are True (this is like AND)
#print(div_by_3.all())
#is there atleast one of the numbers in the array are True (this is like OR)
div_by_3.any()
#Return the sum of all the variables which are True in the array
div_by_3.sum()
#returning all the varibales in the arrays that are True
# this will return the INDEXES of the numbers in the array which are True
#print(div_by_3.nonzero())
#print(np.array(div_by_3.nonzero()))
#In Place = does the function changes the aray or not
#for exaple sort will change the array in place
#x.argsort()
x = m=np.array([4.5, 2.3, 6.7, 1.2, 1.8, 5.5])
# we create a copy of sorted x
np.sort(x)
#print(np.sort(x))
#print(x)
#it show the indexs of the argument that will create us sort method
s = x.argsort()
#print(s)
#print(x[s])
z = np.array([[1.0, 2.0], [4.0, 3.0]])
#print(z)
# all the linear algebra functions
# https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.linalg.html
#print(z.transpose())
#print(np.linalg.inv(z))
z = np.matrix([[1,3], [2,4]])
#print(z)
j = np.eye(3)
#print(j)
A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
#print(A)
B = np.array([[n for n in range(5)] for m in range(5)])
#print(B)
C = np.dot(A,B)
#print(C)



#TRANSPOSE MATRIX
matrixA = np.matrix([[1,2], [3,4]])
#print(matrixA)
matrixA_Trans = np.transpose(matrixA)
#print(matrixA_Trans)
matrixA_Inv = np.linalg.inv(matrixA)
#print(matrixA_Inv)
#DOT MULTIPLACTIOM
iden = matrixA @ matrixA_Inv
#ROUNDING FUNCTION
iden_round = np.around(iden, decimals=1)
#print(iden_round)

MatrixB = np.matrix([[3,-7,-2], [-3,5,1],[6,-4,0]])
MatrixB_Inv = np.linalg.inv(MatrixB)
#print(MatrixB_Inv)


#Solving linear equations
#Example: Solve the system of equations:
#      3 * x0 + x1     = 9
#      x0     + 2 * x1 = 8:
a = np.array([[3,1], [1,2]])
#print(a)
b = np.array([9,8])
x = np.linalg.solve(a, b)
# print(a)
# print(b)
# print(x)
#solotion => X0 = 2, x1 = 3
#meaning 3*(x0=2) + (x1=3) = 3*2 + 3 = 6+3 = 9

#How to check if the slotion in correct
#we just check if a*x == b
#print(np.allclose(np.dot(a, x), b))



A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
P, L, U = scipy.linalg.lu(A)
#
# print("A:")
# #pprint.pprint(A)
# print(A)
# print("P:")
# #pprint.pprint(P)
# print(P)
# print("L:")
# #pprint.pprint(L)
# print(L)
# print("U:")
# #pprint.pprint(U)
# print(U)
# #Checking if indeed P*L*U == A
# print(np.allclose(A - P @ L @ U, np.zeros((4, 4))))

#finding magnitude of 2 vectors
a = np.array([1,2])
b = np.array([2,1])
dot_array = a*b
# print(np.sum(a*b))
# print((a*b).sum())
# print(np.dot(a,b))

#Calculate the angle betweeb a and b
#1. We will find the length of the vectors by sqrt((x2-x1)**2 + (y2-y1)**2))
#2.Fnding the cosine of the angle between the vectors using thier length
#3. Find the actual angle between the vectors

#method 1 to find the length
a_magnitude = np.sqrt((a*a).sum())
b_magnitude = np.sqrt((b*b).sum())
#method 2 to find the length
a_mag = np.linalg.norm(a)
#print(a_mag)
# print(a_magnitude)
# print(b_magnitude)
#Finding the cosine of the angle between the vectors
cos_ab = a.dot(b) / (np.linalg.norm(a)*np.linalg.norm(b))
#print(cos_ab)
#Find the actual angle between the vectors
#this Angle is in Radians
ang_a_b = np.arccos(cos_ab)
#print(ang_a_b)
#the angle in degrees
#print(np.rad2deg(ang_a_b))

#random.random() = gives random numbers out of a uniform distributed function
#random.randn() = gives a random number out of a guaissian distrintion function, with mean = 0 and variance = 1
#we must use as G = np.random.randn(m,n) , m= rows, n=columns
#mean value = G.mean()
#Variance value = G.var()

#Outer producr
a = np.array([[1,2],[1,3]])
b = np.array([[3,4], [1,2]])
#print(np.outer(a,b))
#Inner product
#print(np.inner(a,b))
#Trace of a matrix
#print(np.trace(a))

#Finding eignvalues and eigenvectors
X= np.random.randn(100,3)
cov_X = np.cov(X.T)
#print(cov_X.shape)
#print eignvalues
#print(np.linalg.eigh(cov_X))

#Solving a linear system
Mat_A = np.array([[1,2], [3,4]])
VecB_Sol = np.array([1,2])
#In order to solve for X vector in the equation AX = b =>   we denote the equeation X = Inv(A)*b

X_Sol = np.linalg.inv(Mat_A).dot(VecB_Sol)
#print(X_Sol)

#Better way to solve is to use the solve method
X_Sol = np.linalg.solve(Mat_A, VecB_Sol)

#Solotion for Example NUMPY STACK UDEMY
A = np.array([[1,1], [1.5,4]])
b = np.array([2200, 5050])

X_vec_sol = np.linalg.solve(A,b)
print(X_vec_sol)