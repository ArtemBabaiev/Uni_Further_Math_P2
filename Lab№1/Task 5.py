if __name__ == '__main__':
    from sympy import *
    f = input("Введіть функцію: ")
    x = symbols('x')
    integ = integrate(f, x)
    print(str(integ) + " + C")
