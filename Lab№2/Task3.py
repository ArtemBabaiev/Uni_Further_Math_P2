# -*- coding: utf-8 -*-

#y'' = (2*x*y')\(x**2+1)
# y(0) = 1;   y'(0) = 3
# y = x**3 + 3*x +1

def f(x, yn, yn_1, h):
    return (2*x*(yn - yn_1))/(h*(x**2+1))


def GetY(x, yn, yn_1, h):
    return 2*yn-yn_1 + h**2 * f(x, yn, yn_1, h)

import matplotlib.pyplot as plt
from math import *


if True:
    canv = plt.subplot()
    a = 0
    b = 5
    N = 10
    h = (b-a)/N
    y0 = 1
    y1 = 3*h+y0
    arrY = [y0, y1]
    arrX = [0]
    for i in range(N):
        arrX.append(a+i*h)
        if i <= 0:
            continue
        arrY.append(GetY(arrX[i-1], arrY[-1], arrY[-2], h))
    canv.plot(arrX, arrY, "b")
    
    N = 100
    h = (b-a)/N
    y0 = 1
    y1 = 3*h+y0
    arrY = [y0, y1]
    arrX = [0]
    for i in range(N):
        arrX.append(a+i*h)
        if i <= 0:
            continue
        arrY.append(GetY(arrX[i-1], arrY[-1], arrY[-2], h))
    canv.plot(arrX, arrY, "r")
    
    N = 1000
    h = (b-a)/N
    y0 = 1
    y1 = 3*h+y0
    arrY = [y0, y1]
    arrX = [0]
    for i in range(N):
        arrX.append(a+i*h)
        if i <= 0:
            continue
        arrY.append(GetY(arrX[i-1], arrY[-1], arrY[-2], h))
    canv.plot(arrX, arrY, "y")
    
    
    arrX = []
    arrY = []
    i = 0
    while i <= 5:
        arrX.append(i)
        arrY.append(i**3 + 3*i +1)
        i+=0.1
    canv.plot(arrX, arrY, "k")