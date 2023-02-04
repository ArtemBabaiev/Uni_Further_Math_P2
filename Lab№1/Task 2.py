if __name__ == '__main__':
    import cmath

    a_1 = float(input("Дійсна частина числа: "))
    b_1 = float(input("Уявна частина числа: "))
    z_1 = complex(a_1, b_1)

    trig = cmath.polar(z_1)
    print("Тригонометрична форма: " + str(round(trig[0], 3)) + " * (cos(" + str(round(trig[1], 3)) + ") + i*sin(" + str(round(trig[1], 3)) + ")")
    # print("Показникова форма: " + str(round(trig[0], 3)) + " * " + "e^(" + str(round(trig[1], 3)) + "*i)")
