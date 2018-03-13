#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem072 Counting fractions

#欧拉函数之和等于最简真分数个数
n = 1000000
isprime = [True] * (n + 1) #质数标识
isprime[0] = isprime[1] = False
result = [] #质数列表
euler = [0, 0] + list(range(2, n + 1))#欧拉函数表
for i in range(2, n + 1):
    if not isprime[i]:
        continue
    else:
        result.append(i)
        euler[i] = i - 1
        for j in range(i * 2, n + 1, i):
            isprime[j] = False
            euler[j] *= (1 - (1 / i))
print(int(sum(euler)))
#答案：303963552391
