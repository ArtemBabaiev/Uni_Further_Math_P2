import numpy as np
from math import *
import matplotlib.pyplot as plt

# y = (cos(x)/2) - (1/6)*exp(x-3)*(exp(3)*(x-3) + x*(cos(3)-8))

def A_matrix(a,b, h, N):
    """
        a,b - coefficients of the DE:
            y'' +a*y'+b*y = f(x)
        h - step 
        N - number of intervals
    """
    A = np.zeros(shape=(N+1,N+1))
    A[0,0] = 1
    A[-1,-1] = 1
    for i in range(1, N):
        A[i,i] = -2+ a *h +b*h**2
        A[i,i+1] = 1
        A[i,i-1] = 1 - a *h 
    return(A)
    


    
    
if True:
    canv = plt.subplot()
    
    a = 0
    b = 3
    
    N= 5
    h = (b-a)/N
    A = np.linalg.inv(A_matrix(-2,1, h, N))
    arrX =[]
    B = []
    
    for i in range(0, N+1):
        arrX.append(a + h*i)
        if i ==0:
            B.append(1)
        elif i == N:
            B.append(4)
        else:
            B.append((h**2) * sin(arrX[-1]))
    arrY = A.dot(B)
    canv.plot(arrX, arrY, "y")
    
    N= 10
    h = (b-a)/N
    A = np.linalg.inv(A_matrix(-2,1, h, N))
    arrX =[]
    B = []
    
    for i in range(0, N+1):
        arrX.append(a + h*i)
        if i ==0:
            B.append(1)
        elif i == N:
            B.append(4)
        else:
            B.append((h**2) * sin(arrX[-1]))
    arrY = A.dot(B)
    canv.plot(arrX, arrY, "b")
    
    N= 50
    h = (b-a)/N
    A = np.linalg.inv(A_matrix(-2,1, h, N))
    arrX =[]
    B = []
    
    for i in range(0, N+1):
        arrX.append(a + h*i)
        if i ==0:
            B.append(1)
        elif i == N:
            B.append(4)
        else:
            B.append((h**2) * sin(arrX[-1]))
    arrY = A.dot(B)
    canv.plot(arrX, arrY, "g")


    arrY = []
    arrX = []
    x = 0
    while x <= 3:
        arrX.append(x)
        arrY.append((cos(x)/2) - (1/6)*exp(x-3)*(exp(3)*(x-3) + x*(cos(3)-8)))
        x+=0.1
    canv.plot(arrX, arrY, "r")
    
    
    
    
    
    
    
    
    