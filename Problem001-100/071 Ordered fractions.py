#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem071 Ordered fractions

#得到一个数的质因数
def computer(n):
    prilist = []
    startnum = 2
    while startnum ** 2 <= n:
        if n % startnum == 0:
            n = n // startnum
            if startnum not in prilist:
                prilist.append(startnum)
            startnum = 2
        else:
            startnum += 1
    if n not in prilist:
        prilist.append(n)
    return prilist

for iii in range(1000000, 1, -1):
    dd = 3 * iii - 1
    if dd % 7 == 0:
        b1 = computer(iii)
        b2 = computer(dd // 7)
        if len(list(set(b1) & set(b2))) == 0:#求交集
            print('分数为%d/%d'%(dd // 7, iii))
            break
#答案：分数为428570/999997，分子为425870
