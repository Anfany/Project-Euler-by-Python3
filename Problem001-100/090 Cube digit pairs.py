#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem090 Cube digit pairs

import itertools
squre = ['0%d'%(dn ** 2) if len(str((dn ** 2))) == 1 else '%d'%(dn ** 2) for dn in  range(1, 10)]#100以内的平方数

def judge(elist, xlist, dictlist = squre):#
    alllist = []
    #69可颠倒
    if '6' in elist:
        elist.append('9')
    if '9' in elist:
        elist.append('6')
    if '6' in xlist:
        xlist.append('9')
    if '9' in xlist:
        xlist.append('6')
    for ee in elist:
        for xx in xlist:
            alllist.append(ee + xx)
            alllist.append(xx + ee)
    #判断是否可以全部表示
    for dd in dictlist:
        if dd not in alllist:
            return False
    return True

ff = 0
strdigit = [str(i) for i in range(10)]
count = 0
for ii in itertools.combinations(strdigit, 6):#一个立方体10个数中选择6个
    for jj in itertools.combinations(strdigit, 6):#另一个立方体10个数中选择6个
        ff += 1
        if judge(list(ii), list(jj)):#判断是否可以完全表示平方数
            count += 1
print(int(count / 2))#因为多算了一倍
#答案：1217
