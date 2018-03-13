#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem092 Square digit chains

def tonu(number):#数转化为数字平方的和
    if number == 1:
        return False
    elif number == 89:
        return True
    else:
        fu = str(number)
        summ = 0
        for jj in fu:
            summ += int(jj) ** 2
        return tonu(summ)

numdict = {}
for ii in range(1, 10000000):
    fnu = 0
    for jj in str(ii):
        fnu += int(jj) * int(jj)
    try:
        numdict[fnu] += 1
    except KeyError:
        numdict[fnu] = 1

count = 0
for oo in range(1, 7 * 9 * 9 + 1):#小于1000万的数转化之后的范围。
    if tonu(oo):
        try:
            count += numdict[oo]
        except KeyError:
            pass
print(count)
#答案：8581146
