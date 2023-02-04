# -*- coding: utf-8 -*-

#(n+1)*(x+1)^n    -2<x<0

import matplotlib.pyplot as plt


def GetFunction(m: int) -> str:
    formula = "((n+1)*(x+1)**n)"
    result = ""
    for i in range(1, m+1):
        result += formula.replace("n", f"{i}")
        if i != m:
            result += "+"
    return result



a = -1.9
b = 0
arrN = [2,3,5, 10, 20, 50]
colors = ["b", "g", "y", "m", "r", "c" ]

arrX = []
arrY = []
x = -1.9
while x < -0.1:
    arrX.append(x)
    arrY.append(1/(x**2))
    x+=0.01
plt.plot(arrX, arrY, "k", linewidth = 5, label = "f(x)")

for i in range(len(arrN)):
    arrX = []
    arrY = []
    x = a
    formul = GetFunction(arrN[i])
    while x < -0.1:
        arrX.append(x)
        arrY.append(eval(formul))
        x += 0.01
    plt.plot(arrX, arrY, colors[i], label = f"m={arrN[i]}",linestyle="--")
plt.legend()
plt.show()


a = -1.5
b = -0.1

arrR = []
for i in range(len(arrN)):
    arrY = []
    arrYm = []
    formul = GetFunction(arrN[i])
    x= a
    while x<b:
        arrY.append(eval("1/x**2"))
        arrYm.append(eval(formul))
        x+=0.1
    biggest = -1
    for i in range(len(arrY)):
        if abs(arrY[i] - arrYm[i])>=biggest:
            biggest = abs(arrY[i] - arrYm[i])
    arrR.append(biggest)
plt.plot(arrN, arrR)









