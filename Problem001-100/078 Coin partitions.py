#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem078 Coin partitions

def Tran(n):
    if n == 0:
        return 1
    else:
        return int((3 * n * n - n) / 2)
exlist ={0 : 1}
num = 1
while 1:
    n = 1
    star = 0
    while num - Tran(n) >= 0:
        star += int((-1 * (-1) ** (n))) * exlist[num - Tran(n)]
        if n <= 0:
            n = -n + 1
        else:
            n = -n
    exlist[num] = int(star)
    if str(exlist[num])[-6:] == '000000':#被100万整除
        break
    num += 1
print(num)
print(exlist[num])
#答案：最小的n：55374
#p(55374)=36325300925435785930832331577396761646715836173633893227071086460709268608053489541731404543537668438991170680745272159154493740615385823202158167635276250554555342115855424598920159035413044811245082197335097953570911884252410730174907784762924663654000000
