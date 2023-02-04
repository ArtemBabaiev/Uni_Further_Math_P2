# -*- coding: utf-8 -*-

# y' = (y+x*sin(y/x))/x
# y(1) = pi/2
# y = 2*x*acot(1/x)

import matplotlib.pyplot as plt
from math import *
import sympy

def Y(x):
    try:
        temp = 2*x*sympy.acot(1/x)
    except ZeroDivisionError:
        return 0
    else:
        return temp

def dy(x, y):
    return (y+x*sin(y/x))/x

def GetY(prevX, prevY, h):
    k1 = dy(prevX, prevY)
    k2 = dy(prevX+0.5*h, prevY+0.5*h*k1)
    k3 = dy(prevX+0.5*h, prevY+0.5*h*k2)
    k4 = dy(prevX+h, prevY+h*k3)
    return prevY + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

if True:
    canv = plt.subplot()
    a = 1
    b = 3
    
    
    arrX = []
    arrY = []    
    x = 1
    while(x<=3):
        arrX.append(x)
        arrY.append(Y(x))
        x+=0.1
    #canv.plot(arrX, arrY, "r")
    
    N = 10
    h = (b-a)/N
    arrX = [1]
    arrY = [pi/2]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY.append(GetY(arrX[i-1], arrY[-1], h))
    #canv.plot(arrX, arrY, "b")   
    
    N = 100
    h = (b-a)/N
    arrX = [1]
    arrY = [pi/2]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY.append(GetY(arrX[i-1], arrY[-1], h))
    canv.plot(arrX, arrY, "y")   
    
    N = 1000
    h = (b-a)/N
    arrX = [1]
    arrY = [pi/2]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY.append(GetY(arrX[i-1], arrY[-1], h))
    #canv.plot(arrX, arrY, "g")   
    
    
    
    
    