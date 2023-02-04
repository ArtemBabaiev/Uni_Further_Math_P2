if __name__ == '__main__':
    import cmath
    import math
    a_1 = float(input("Дійсна частина першого числа: "))
    b_1 = float(input("Уявна частина першого числа: "))
    a_2 = float(input("Дійсна частина другого числа: "))
    b_2 = float(input("Уявна частина другого числа: "))
    operation = input("Введіть операцію: ")

    z_1 = complex(a_1, b_1)
    z_2 = complex(a_2, b_2)

    if operation == "+":
        result = z_1+z_2
    elif operation == "-":
        result = z_1-z_2
    elif operation == "*":
        result = z_1*z_2
    elif operation == "/":
        result = z_1/z_2
    else:
        print("Неправильно введена операція")
    print("\nРезультат:")
    print("\tАлгебраїчна " + str(result))
    # print("Результат: " + str(result.real) + " + " +str(result.imag) + "*i")
    r = round((result.real**2 + result.imag**2)**0.5, 3)
    if result.real < 0:
        phi = round(math.atan(result.imag/result.real) + math.pi, 3)
    else:
        phi = round(math.atan(result.imag / result.real), 3)
    print ("\tТригонометрична: " +str(r) + "*(cos(" + str(phi) + ") + j*sin(" + str(phi) + ")")
