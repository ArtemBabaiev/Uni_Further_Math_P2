# -*- coding: utf-8 -*-
# y' = -(3*exp(x) * sin(y)* cos(y))/(1+exp(x))
# y(0) = pi/4
# y = acot(((1+exp(x))**3)/8)

import matplotlib.pyplot as plt
from math import *
import sympy
def Y(x):
    return sympy.acot(((1+exp(x))**3)/8)

def dy(x, y):
    return -(3*exp(x) * sin(y)* cos(y))/(1+exp(x))

def getY(prevX, prevY, h):
    return prevY + h*dy(prevX, prevY)


if True:
    canv = plt.subplot()
    b = 15
    a = 0
    N=10
    h = (b-a)/N
    arrX = [0]
    arrY = [pi/4]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY.append(getY(arrX[i-1], arrY[-1], h))
    print(arrX)
    print(arrY)
    canv.plot(arrX, arrY, "y")
    
    N = 100
    h = (b-a)/N
    arrX = [0]
    arrY = [pi/4]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY.append(getY(arrX[i-1], arrY[-1], h))
    canv.plot(arrX, arrY, "b")
    
    N = 1000
    h = (b-a)/N
    arrX = [0]
    arrY = [pi/4]
    for i in range(1, N+1):
        arrX.append(a+i*h)
        arrY.append(getY(arrX[i-1], arrY[-1], h))
    canv.plot(arrX, arrY, "g")
    
    
    arrX = []
    arrY = []
    x=0
    
    while x<=b:
        arrX.append(x)
        arrY.append(Y(x))
        x+=0.1
    canv.plot(arrX, arrY, "r")
    
    
    
    
        
    
    
    
    
    
    
    
    
#    N = 10
#    b = 15
#    h=b/N
#    x0 = 0
#    y0 = pi/4
#    arr_x = [0]
#    arr_y = [pi/4]
#    i=0
#    
#    while x0<b:
#        arr_y.append(getY(arr_x[i], arr_y[i], h))
#        x0 = x0+(i+1)*h
#        arr_x.append(x0)
#    print(arr_x)
#    print(arr_y)
#    canv.plot(arr_x, arr_y, "b")
    
    
