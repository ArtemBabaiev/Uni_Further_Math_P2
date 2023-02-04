from sympy import *
from math import *
if __name__ == '__main__':
    t = Symbol('T')
    x = input("x = ")
    y = input("y = ")
    z = input("z = ")
    b = float(input("Введіть верхню межу: "))
    a = float(input("Введіть нижню межу: "))
    difx = diff(x, t)
    dify = diff(y, t)
    difz = diff(z, t)
    forinteg = "(" + "(" + str(difx) + ")**2 + " + "(" + str(dify) + ")**2 + " + "(" + str(difz) + ")**2)**0.5"
    print(forinteg)
    sum = 0
    num = 100
    h = (b - a) / num
    for i in range(num):
        ti = a + i * h
        toEval = forinteg.replace('T', str(ti))
        sum += h * eval(toEval)
    print("Значення: " + str(sum))