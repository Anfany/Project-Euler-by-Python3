#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem087 Prime power triples

import numpy as np
import itertools
def Comprime(m, s):#得到素数的s次方
    n = int(m ** (1 / s)) + 1
    isprime = [True] * (n + 1)  # 质数标识
    isprime[0] = isprime[1] = False
    result = []  # 质数列表
    for i in range(2, n + 1):
        if not isprime[i]:
            continue
        else:
            result.append(i)
            for j in range(i * 2, n + 1, i):
                isprime[j] = False
    return np.array(result) ** s

squre = Comprime(50000000, 2)#平方
cube = Comprime(50000000, 3)#立方
forth = Comprime(50000000, 4)#四次方

print((len(set(sum(list(i)) for i in itertools.product(squre, cube, forth) if sum(list(i)) < 50000000))))
#答案：1097343
