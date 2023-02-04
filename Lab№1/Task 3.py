if __name__ == '__main__':
    import cmath
    from math import sin, cos
    r = float(input("Модуль дійсного числа: "))
    phi = float(input("Кут: "))
    z = cmath.rect(r, phi)
    altZ = r*(cos(phi) + sin(phi)*1j)
    print("Алгебраїчна форма: " + str(z))
    print(altZ)
