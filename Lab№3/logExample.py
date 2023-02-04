# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:35:23 2021

@author: User
"""

from scipy.integrate import quad
import matplotlib.pyplot as plt
from numpy import log
from  math import sin, cos, pi

def getAn(x, l, h, n):
    return log(x+h)*cos((pi*n*x)/l)

def getBn(x, l, h, n):
    return log(x+h)*sin((pi*n*x)/l)
    
def getA0(x,h):
    return log(x+h)

canv = plt.subplot()
a = 0.2
b = 2
l = (b-a)/2
h = (a+b)/2
arrN = [2,3,5, 10, 20, 50]
colors = ["b", "g", "y", "m", "c", "r" ]
arrX = []
arrY = []
x = a
while x < b:
    arrX.append(x)
    arrY.append(log(x))
    x+=0.05
canv.plot(arrX, arrY, "k", linewidth = 4, label = "f(x)")


A0 = (1/l) * quad(getA0, -l, l, args = (h))[0]
for i in range(len(arrN)):
    arrX = []
    arrY = []
    x = a
    formul = ""
    for j in range(1, arrN[i] + 1):
        An = (1/l) * quad(getAn, -l, l, args = (l, h, j))[0]
        Bn = (1/l) * quad(getBn, -l, l, args = (l, h, j))[0]
        formul += f"{An}*cos((pi*{j}*(x - h))/l) + {Bn}*sin((pi*{j}*(x - h))/l)"
        #formul += f"{An}*cos((pi*{j}*(x - h))/l)"
        if j!=arrN[i]:
            formul+="+"
    while x<b:
        arrX.append(x)
        arrY.append(A0/2 + eval(formul))
        x+=0.05
    canv.plot(arrX, arrY, colors[i], label = f"m={arrN[i]}",linestyle="--")
plt.legend()