#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem073 Counting fractions in a range

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
count = 0
for ii in range(4, 12001):
    for gg in range(int(ii / 3) + 1, int(ii / 2) + 1):#在三分之一和二分之一之间
        if Euclidean(ii, gg) == 1:
            count += 1
print(count)
#答案：7295372
