# -*- coding: utf-8 -*-
#1/x^2   -2<x<0
#(n+1)*(x+1)^n    -2<x<0

from scipy.integrate import quad
import matplotlib.pyplot as plt
from  math import *

def getAn(x, l, h, n):
    return (1/(x+h)**2)*cos((pi*n*x)/l)

def getBn(x, l, h, n):
    return (1/(x+h)**2)*sin((pi*n*x)/l)
    

canv = plt.subplot()
a = -1.9
b = -0.1
l = (b-a)/2
h = (a+b)/2
arrN = [2,3,5, 10, 20, 200]
colors = ["b", "g", "y", "m", "c", "r" ]
arrX = []
arrY = []
x = a
while x < b:
    arrX.append(x)
    arrY.append(1/(x**2))
    x+=0.05
canv.plot(arrX, arrY, "k", linewidth = 4, label = "f(x)")


A0 = (1/l) * quad(getAn, -l, l, args = (l, h, 0))[0]
for i in range(len(arrN)):
    arrX = []
    arrY = []
    x = a
    formul = ""
    for j in range(1, arrN[i] + 1):
        An = (1/l) * quad(getAn, -l, l, args = (l, h, j))[0]
        Bn = (1/l) * quad(getBn, -l, l, args = (l, h, j))[0]
        formul += f"{An}*cos((pi*{j}*(x - h))/l) + {Bn}*sin((pi*{j}*(x - h))/l)"
        if j!=arrN[i]:
            formul+="+"
    while x<b:
        arrX.append(x)
        arrY.append(A0/2 + eval(formul))
        x+=0.05
    canv.plot(arrX, arrY, colors[i], label = f"m={arrN[i]}",linestyle="--")
plt.legend()
            
            
            
            
            
            
            
            
            
            