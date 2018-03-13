#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem083 Path sum four ways

import numpy as np
fan=open(r'C:\Users\GWT9\Desktop\p083_matrix.txt')
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
npan = np.array(an, dtype=int)#转化为np数组形式转置
copynpan = np.array(npan.copy(), dtype = float)
#开始
zuibiaoset = []
for jj in range(len(npan)):
    for gg in range(len(npan)):
        copynpan[jj, gg] = float('inf')
copynpan[0, 0] = npan[0, 0]
#构建联通字典
liantong = {}
for gg in range(len(npan)):
    for hh in range(len(npan)):
        dd = [[gg - 1, hh],[gg + 1, hh],[gg, hh - 1],[gg, hh + 1]]
        liantong[(gg, hh)] = []
        for ff in dd:
            if ff[0] >=0 and ff[0] < len(npan) and ff[1] >=0 and ff[1] < len(npan):
                liantong[(gg, hh)].append(ff)
#Dijkstra 算法
def Dijkstra(startlist, lidict = liantong, yuanshi = npan, com = copynpan):
    start = []
    if startlist == []:
        return com
    else:
        for gg in startlist:
            fulist = lidict[(gg[0], gg[1])]
            for jjj in fulist:
                comnumber = com[gg[0], gg[1]] + yuanshi[jjj[0], jjj[1]]
                if comnumber < com[jjj[0], jjj[1]]:
                    com[jjj[0], jjj[1]] = comnumber
                    start.append(jjj)
    return Dijkstra(start)
print(int(Dijkstra([[0, 0]])[-1,-1]))
#答案：425185
