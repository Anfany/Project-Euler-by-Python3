#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem003 Largest prime factor
def getfactor(num):
    arr = []
    i = 2
    while num != 1:
        if num % i == 0:
            while num % i == 0:
                arr.append(i)
                num /= i
        i = i + 1
    return  max(arr)
print(getfactor(600851475143))

#答案：6857
