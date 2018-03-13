#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem077 Prime summations

def Prime(number):#素数序列
    isprime = [False, False] + [True] * (number - 1)
    prime = []
    for ii in range(2, number + 1):
        if isprime[ii]:
            prime.append(ii)
            for jj in range(ii * 2, number + 1, ii):
                isprime[jj] = False
    return prime

def DP_Com(exlist,num):#动态规划
    an=[1]+[0]*num
    for i in exlist :
        for j in range(i,num+1):
            an[j]+=an[j-i]
    return an[num]
count = 0
number = 9
while count <= 5000:
    number += 1
    count = DP_Com(Prime(number), number)
print(number)
#答案：71
