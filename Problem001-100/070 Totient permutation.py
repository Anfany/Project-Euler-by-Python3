#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem070 Totient permutation

n = 10000000
isprime = [True] * (n + 1) #质数标识
isprime[0] = isprime[1] = False
result = [] #质数列表
euler = [n, n] + list(range(2, n + 1))#欧拉函数表

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
funceuler = {i : i /euler[i]  for i in range(0, n + 1) if sorted(str(i)) == sorted(str(int(euler[i])))}#只选择φ(n)和n是重排的.

minkey = min(funceuler.items(), key = lambda x : x[1])[0]
print(euler[minkey])
print(minkey)
#答案：φ(8319823)=8313928
#最小的n值为8319823
