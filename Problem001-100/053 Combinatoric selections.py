#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem053 Combinatoric selections

def GetComb(m, n):  # 计算数的组合值
    pro = 1
    orp = 1
    for i in range(m + 1 - n, m + 1):
        pro *= i
    for j in range(1, n + 1):
        orp *= j
    return pro / orp
ji = 0
for i in range(1, 101):
    for j in range(1, i):
        if GetComb(i, j) >= 1e6:
            ji += 1
print(ji)
#答案：4075
