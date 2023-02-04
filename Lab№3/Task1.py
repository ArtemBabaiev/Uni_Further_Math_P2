# -*- coding: utf-8 -*-

# 1/((n+1)*(n+2)*(n+3))

import matplotlib.pyplot as plt

def GetSum(maxi: int) -> int:
    summ = 0
    for i in range(1, maxi+1):
        summ += 1/((i+1)*(i+2)*(i+3))
    return summ


if True:
    canv = plt.subplot()
    arrX = []
    arrY = []
    m = 8
    eps = 0.00001
    while True:
        S = GetSum(m)
        S2 = GetSum(2*m)
        
        arrY.append(S)
        arrX.append(m)
        arrY.append(S2)
        arrX.append(m*2)
        
        if abs(S2-S)<eps:
            break
        m*=2
    print(2*m)
    print(f"S = {S2}")
    canv.plot(arrX, arrY, "r")