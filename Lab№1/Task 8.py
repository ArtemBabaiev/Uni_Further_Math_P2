from sympy import *
from sympy.solvers import solve
from sympy.plotting import plot
from math import *


if __name__ == '__main__':
    x = symbols('x')
    fx = input("f(x) = ")
    gx = input("g(x) = ")
    d = fx+'-('+gx+')'
    print(d)
    cross = solve(d, x)
    print(cross)
    if len(cross) == 2:
        print("Значення: " + str(abs(float(integrate(d, (x, eval(str(cross[0])), eval(str(cross[1]))))))))
    else:
        b = float(input("Введіть верхню межу: "))
        a = float(input("Введіть нижню межу: "))
        print("Значення: " + str(abs(float(integrate(d, (x, b, a))))))
    p1 = plot(fx, show=False)
    p2 = plot(gx, show=False)
    p1.append(p2[0])
    p1.show()

