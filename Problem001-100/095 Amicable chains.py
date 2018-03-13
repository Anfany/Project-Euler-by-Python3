#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem095 Amicable chains

maxnum = 1000000
factorsum = [0, 1] + [0] * (maxnum - 2)
for i in range(1, maxnum):
    for j in range(i * 2, maxnum, i):
        factorsum[j] += i
#开始计算最长链的最小值
minnum = 0
leng = 0
allist = []
for kk in range(2, maxnum):
    sign = 1
    falist = []
    clo = factorsum[kk]
    copynum = clo
    while clo not in falist:#判断是否重复，终止链
        falist.append(clo)
        if clo > 1e6 or clo == 1:
            sign = 0
            break
        clo = factorsum[clo]
    if sign and clo - copynum == 0:#开始结束均为同一个数
        length = len(falist)
        if length > leng:#选取最长的链
            leng = length
            minnum = min(falist)
print(minnum)
#答案：14316
