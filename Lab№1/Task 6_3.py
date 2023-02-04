from math import *

def integral(Fx, higher, lower, symb):
    num_of_figures = 1000
    h = (higher-lower) / num_of_figures
    sum_of_elem = 0
    for i in range(0, num_of_figures):
        xi = lower + i*h
        toEval1 = Fx.replace(symb, str(xi))
        xip1 = lower + (i+1) * h
        toEval2 = Fx.replace(symb, str(xip1))
        xPx = (xi+xip1)/2
        toEval3 = Fx.replace(symb, str(xPx))
        sum_of_elem+= (h/6)*(eval(toEval1) + 4*eval(toEval3) + eval(toEval2))

    return sum_of_elem


if __name__ == '__main__':
    func = input("Введіть функцію: ")
    b = float(input("Введіть верхню межу: "))
    a = float(input("Введіть нижню межу: "))
    print(func)
    if b == float("inf") or a == float("inf") or b == float("-inf") or a == float("-inf"):
        if b == float("inf"):
            b = pi / 2
        elif b == float("-inf"):
            b = -pi / 2
        else:
            b = atan(b)
        if a == float("inf"):
            a = pi / 2
        elif a == float("-inf"):
            a = -pi / 2
        else:
            a = atan(a)
        with_tan = func.replace('X', "tan(T)")
        with_tan = '(' + with_tan + ')/(cos(T)**2)'
        print(with_tan)
        print("Значення: " + str(integral(with_tan, b, a, "T")))
    else:
        print("Значення: " + str(integral(func, b, a, "X")))