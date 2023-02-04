# -*- coding: utf-8 -*-
# y(y')^2 + 2xy - y = 0
# y(0) = 5^0.5


import matplotlib.pyplot as plt
from math import *
import sympy

def Y1(x):
    return (4+2*x*sqrt(5))**0.5
    #return -1j*(5**0.25) * (-(5**0.5) - 2*x)**0.5
def Y2(x):
    return (4-2*x*sqrt(5))**0.5
    #return (5**0.25) * ((5**0.5) - 2*x)**0.5

def dy1(x, y):
    return (-x+sqrt(x*x+y*y))/y
def dy2(x, y):
    return (-x-sqrt(x*x+y*y))/y

def getY1(prevX, prevY, h):
    k1 = dy1(prevX, prevY)
    k2 = dy1(prevX+0.5*h, prevY+0.5*h*k1)
    k3 = dy1(prevX+0.5*h, prevY+0.5*h*k2)
    k4 = dy1(prevX+h, prevY+h*k3)
    return prevY + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
def getY2(prevX, prevY, h):
    k1 = dy2(prevX, prevY)
    k2 = dy2(prevX+0.5*h, prevY+0.5*h*k1)
    k3 = dy2(prevX+0.5*h, prevY+0.5*h*k2)
    k4 = dy2(prevX+h, prevY+h*k3)
    return prevY + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    
if True:
    canv = plt.subplot()
    b = 5
    a = 0
    
    arrX = []
    arrY1 = []
    arrY2 = []    
    i = 0
    while(i<=5):
        arrX.append(i)
        arrY1.append(Y1(i))
        arrY2.append(Y2(i))
        i+=0.1
        
    canv.plot(arrX, arrY1, "r")
    #canv.plot(arrX, arrY2, "r")
    
    N=10
    h = (b-a)/N
    arrX = [0]
    arrY1 = [5**0.5]
    arrY2 = [5**0.5]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY1.append(getY1(arrX[i-1], arrY1[-1], h))
        arrY2.append(getY2(arrX[i-1], arrY2[-1], h))
    canv.plot(arrX, arrY1, "y")
    #canv.plot(arrX, arrY2, "y")

    b = 5
    a = 0
    N=100
    h = (b-a)/N
    arrX = [0]
    arrY1 = [5**0.5]
    arrY2 = [5**0.5]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY1.append(getY1(arrX[i-1], arrY1[-1], h))
        arrY2.append(getY2(arrX[i-1], arrY2[-1], h))
    canv.plot(arrX, arrY1, "b")
   # canv.plot(arrX, arrY2, "b")

    b = 5
    a = 0
    N=1000
    h = (b-a)/N
    arrX = [0]
    arrY1 = [5**0.5]
    arrY2 = [5**0.5]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY1.append(getY1(arrX[i-1], arrY1[-1], h))
        arrY2.append(getY2(arrX[i-1], arrY2[-1], h))
    canv.plot(arrX, arrY1, "g")
    #canv.plot(arrX, arrY2, "g")


    
    