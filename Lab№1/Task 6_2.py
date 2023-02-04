from math import *

def integral(Fx, higher, lower, num, symb):
    h = (higher-lower) / num
    sum_of_elem = 0
    for i in range(0, num):
        xi = lower + i*h
        toEval1 = Fx.replace(symb, str(xi))
        xip1 = lower + (i+1) * h
        toEval2 = Fx.replace(symb, str(xip1))
        sum_of_elem += 0.5 * h * (eval(toEval1) + eval(toEval2))
    return sum_of_elem


if __name__ == '__main__':
    func = input("Введіть функцію: ")
    b = float(input("Введіть верхню межу: "))
    a = float(input("Введіть нижню межу: "))
    num_of_figures = int(input("Введіть кількість трапецій: "))
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
        print("Значення: " + str(integral(with_tan, b, a, num_of_figures, "T")))
    else:
        print("Значення: " + str(integral(func, b, a, num_of_figures, "X")))
