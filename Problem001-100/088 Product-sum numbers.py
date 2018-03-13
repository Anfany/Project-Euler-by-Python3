#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem088 Product-sum numbers

#获得一个数除去本身和1之外的含有2个因子的列表
def fact(n):
    factlist = []
    for jj in range(2, int(n ** 0.5) + 1):
        if n % jj == 0:
            factlist.append([jj, n // jj])
    return factlist
#分解字典
fadict = {}
for i in range(24001):
    fadict[i] = fact(i)
#获得一个数的所有因子乘积表达式
for ii in fadict:
    if len(fadict[ii]) == 0:
        pass
    else:
        falist = []
        for jj in fadict[ii]:
            lelist = len(jj)
            pisk = fadict[jj[-1]]
            if len(pisk) != 0:
                for dd in pisk:
                    cc = jj[: lelist - 1] + dd
                    falist.append(cc)
        fadict[ii] += falist
#开始计算
resultdict ={}
for ike in range(2, 24001):
    if len(fadict[ike]) == 0:
        pass
    else:
        for jjj in fadict[ike]:
            cc = ike - sum(jjj) + len(jjj)
            try:
                if resultdict[cc] > ike:
                    resultdict[cc] = ike
            except KeyError:
                resultdict[cc] = ike

cdict = {i: resultdict[i] for i in resultdict if i <= 12000}
print(sum(list(set(list(cdict.values())))))#无重复元素集合的元素的和
#答案：7587457
