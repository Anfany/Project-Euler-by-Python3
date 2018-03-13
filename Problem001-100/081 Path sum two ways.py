#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem081 Path sum two ways

import numpy as np
fan=open(r'C:\Users\GWT9\Desktop\p081_matrix.txt')
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

npan = np.array(an, dtype=int)#转化为np数组形式
#从左上角开始生成斜线坐标直到右下角
weizhi = []
for jj in range(2 * len(npan) - 2):
    sonweizhi = []
    if jj < len(npan):
        for dd in range(jj + 1):
            sonweizhi.append([dd, jj - dd])
    else:
        for dd in range(jj - len(npan) + 1, len(npan)):
            sonweizhi.append([dd, jj - dd])
    weizhi.append(sonweizhi)
weizhi.append([[len(npan) -1, len(npan) - 1]])

#开始逐斜线计算直到右下角【动态规划思想】
for jj in weizhi[1:]:
    for ii in jj:
        if ii[0] == 0:
            npan[ii[0], ii[1]] += npan[ii[0], ii[1] - 1]
        elif ii[1] == 0:
            npan[ii[0], ii[1]] += npan[ii[0] -1, ii[1]]
        else:
            npan[ii[0], ii[1]] += min(npan[ii[0] -1, ii[1]], npan[ii[0], ii[1] - 1])
#输出最终的结果
print(npan[len(npan) -1, len(npan) - 1])
#答案：427337
