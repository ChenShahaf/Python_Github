#===============================================================================
#=============MACHINE LEARNING NORMAL QEUATION =================================
#                                                                           ====
#             x0   x1   x2   x3   x4   y                                    ====
#             ===========================                                   ====
#              1   2104  5   1    45   460                                  ====
#              1   1416  3   2    40   232                                  ====
#              1   1534  3   2    30   315                                  ====
#              1    852  2   1    36   178                                  ====
#===============================================================================
import numpy as np
#Creating X design matrix
x1 = np.array([2104, 1416, 1534, 852], dtype=np.float32)
x2 = np.array([5, 3, 3, 2], dtype=np.float32)
x3 = np.array([1, 2, 2, 1], dtype=np.float32)
y = np.array([460, 232, 315, 178], dtype=np.float32).reshape((4,1))
#y = np.array([460, 232], dtype=np.float32).reshape((2,1))
np.set_printoptions(suppress=True)
X = np.column_stack((x1,x2))

#print(y)
#Theta is N*1
theta = np.array([1, 1], dtype=np.float32).reshape((2,1))
#print(theta)
#X is an M*N in this case we choose 2 fetures, 4 instances
#print(X)


#print(np.dot(X,theta))

#print(np.dot(X,theta) - y)
print(np.dot(X.T, (np.dot(X,theta) - y)))


def GradientDecent(X,y,start,rate,epochs):
    t=start.copy()
    loss = 0
    for epoch in range(epochs):
        res=np.dot(X,t)
        print(res)
        loss = 0.5 * ((res - y) ** 2).mean()
        #grad=(np.dot(X,res-y))/len(X)
        t=t -rate*grad
    print("GRADIENT DESCENT - The loss for {} No. of iterations is {}, | Learning rate = {} ".format(epochs,loss,rate))
    print("GRADIENT DESCENT - The new \u0275 is {}".format(t))

#GradientDecent(X,y,theta,0.1,100)


import numpy as np
from random import sample
import math


def adagrad(f_grad, x0, data, args, stepsize=1e-2, fudge_factor=1e-6, max_it=1000, minibatchsize=None,
            minibatch_ratio=0.01):
    # f_grad returns the loss functions gradient
    # x0 are the initial parameters (a starting point for the optimization)
    # data is a list of training data
    # args is a list or tuple of additional arguments passed to fgrad
    # stepsize is the global stepsize for adagrad
    # fudge_factor is a small number to counter numerical instabiltiy
    # max_it is the number of iterations adagrad will run
    # minibatchsize if given is the number of training samples considered in each iteration
    # minibatch_ratio if minibatchsize is not set this ratio will be used to determine the batch size dependent on the length of the training data

    # d-dimensional vector representing diag(Gt) to store a running total of the squares of the gradients.
    gti = np.zeros(x0.shape[0])

    ld = len(data)
    if minibatchsize is None:
        minibatchsize = int(math.ceil(len(data) * minibatch_ratio))
    w = x0
    for t in xrange(max_it):
        s = sample(xrange(ld), minibatchsize)
        sd = [data[idx] for idx in s]
        grad = f_grad(w, sd, *args)
        gti += grad ** 2
        adjusted_grad = grad / (fudge_factor + np.sqrt(gti))
        w = w - stepsize * adjusted_grad
    return w
