from sympy import *
import math
if __name__ == '__main__':

    func = input("Введіть функцію: ")
    b = eval(input("Введіть верхню межу: "))
    a = float(input("Введіть нижню межу: "))
    accuracy = int(input("Введіть кількість прямокутників: "))
    print(func)
    if b == float("inf") or a == float("inf") or b == float("-inf") or a == float("-inf"):
        with_tan = func.replace('X', "math.tan(T)")
        if b == float("inf"):
            b = math.pi/2
        elif b == float("-inf"):
            b = -math.pi/2
        else:
            b = math.atan(b)
        if a == float("inf"):
            a = math.pi/2
        elif a == float("-inf"):
            a = -math.pi/2
        else:
            a = math.atan(a)
        with_tan = '(' + with_tan + ')/(math.cos(T)**2)'
        print(with_tan)
        sum = 0
        h = (b - a) / accuracy
        for i in range(accuracy):
            ti = a + i * h
            toEval = with_tan.replace('T', str(ti))
            #toEval = "abs(" + toEval + ")"
            sum += h * eval(toEval)
        print("Значення: " + str(sum))
    else:
        sum = 0
        h = (b - a) / accuracy
        for i in range(accuracy):
            xi = a + i * h
            toEval = func.replace('X', str(xi))
            sum += h * eval(toEval)
        print("Значення: " + str(sum))

