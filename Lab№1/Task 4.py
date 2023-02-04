if __name__ == '__main__':
    import cmath
    import math
    a_1 = float(input("Дійсна частина числа: "))
    b_1 = float(input("Уявна частина числа: "))
    degree = float(input("Введіть степінь числа: "))

    z_1 = complex(a_1, b_1)
    trig = cmath.polar(z_1)
    print(trig)
    if abs(degree)>0 and abs(degree)<1:
        n = int(1/degree)
        for k in range(1, n+1):
            Res = abs(trig[0] ** degree) * (math.cos((trig[1]+2*math.pi*k)/n) + 1j*math.sin((trig[1]+2*math.pi*k)/n))
            print(Res)
    else:
        Res = abs(trig[0] ** degree) * (math.cos(trig[0]*degree) + 1j*math.sin(trig[0]*degree))







