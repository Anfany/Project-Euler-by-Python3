#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem069 Totient maximum

n = 1000000
isprime = [True] * (n + 1) #质数标识
isprime[0] = isprime[1] = False
result = [] #质数列表
euler = [1, 1] + list(range(2, n + 1))#欧拉函数表

for i in range(2, n + 1):
    if not isprime[i]:
        continue
    else:
        result.append(i)
        euler[i] = i - 1
        for j in range(i * 2, n + 1, i):
            isprime[j] = False
            euler[j] *= (1 - (1 / i))
#n/φ(n)
funceuler = {i : i /euler[i] for i in range(0, n + 1)}#计算n/φ(n)
print(max(funceuler.items(), key = lambda x : x[1])[0])#计算n/φ(n)最大值对应的n值
#答案：510510
