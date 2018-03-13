#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem082 Path sum three ways

import numpy as np
fan=open(r'C:\Users\GWT9\Desktop\p082_matrix.txt')
an =[]
#读取数据
while 1:
    x=fan.readline()
    if len(x) == 0:
        break
    du = []
    for jjj in list(x.split(',')):
        du.append(jjj)
    an.append(du)
fan.close()
npan = np.array(an, dtype=int).T#转化为np数组形式转置
copynpan = npan.copy()
#定义组合函数
def combine(nplist, mcode):
    comlist = []
    for i in range(len(nplist)):
        dnum = 0
        if i < mcode:
            cc = i + 1
            while cc < mcode:
                dnum += nplist[cc]
                cc += 1
            comlist.append(dnum)
        elif i == mcode:
            pass
        else:
            cc = i - 1
            while cc > mcode:
                dnum += nplist[cc]
                cc -= 1
            comlist.append(dnum)
    return comlist

for jj in range(1, len(npan)):#开始逐行进行计算【动态规划】
    for gg in range(len(npan[jj])):#直接运算
        npan[jj, gg] += npan[jj-1, gg]
    if jj < len(npan) - 1:
        Dcopynpan = copynpan.copy()
        for ii in range(len(npan[jj])):#开始比较运算
            if ii == 0:
                copynpan[jj, ii] += min(copynpan[jj - 1, ii], np.min(npan[jj][1 :] + np.array(combine(Dcopynpan[jj], ii))))#需要比较所有路径
            elif ii == len(npan[jj]) - 1:
                copynpan[jj, ii] += min(copynpan[jj - 1, ii], np.min(npan[jj][: -1] + np.array(combine(Dcopynpan[jj], ii))))#需要比较所有路径
            else:
                addlist = np.array(list(npan[jj][: ii]) + list(npan[jj][ii + 1 :]))
                copynpan[jj, ii] += min(copynpan[jj - 1, ii], np.min(np.array(combine(Dcopynpan[jj], ii)) + addlist))#需要比较所有路径
        npan = copynpan.copy()
    else:
        print(np.min(npan[-1]))
#答案：260324
