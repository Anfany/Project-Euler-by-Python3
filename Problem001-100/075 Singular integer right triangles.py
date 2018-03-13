#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem075 Singular integer right triangles

number = 1500000
fu = [0 for i in range(0, number + 1)]
count = 0
#辗转相除法计算最大公因数
def Euclidean(a, b):
    d = a % b
    if d == 0:
        return b
    else:
        while d != 0:
            a, b = b, a % b
            d = a % b
        return b
for iii in range(2, int((number / 2) ** 0.5)):
    for jjj in range(1, iii):
        if (iii + jjj) % 2 == 1 and Euclidean(jjj, iii) == 1:
            ee = 2 * iii * jjj
            ff = iii ** 2 - jjj ** 2
            dd = jjj ** 2 + iii ** 2
            ssum = int(ee + dd + ff)
            if ssum < number:
                for jj in range(ssum, number, ssum):#所有解
                    fu[jj] += 1
            else:
                break
print(fu.count(1))#只有一种解的个数
#答案：161667
