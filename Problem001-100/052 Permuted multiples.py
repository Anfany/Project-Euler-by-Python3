#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem052 Permuted multiples

def SameDigit(exlist):#判断数字相同
    for i in  exlist:
        if set(i)!=set(exlist[0]):
            return False
    return True
Number=1
while 1:
    Nlist=[str(i*Number) for i in range(1,7)]
    if SameDigit(Nlist):
        print(Nlist)
        break
    else:
        Number+=1
#答案：['142857', '285714', '428571', '571428', '714285', '857142']
#结果：142857.
