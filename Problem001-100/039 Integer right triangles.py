#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem039 Integer right triangles

anfan, exdict = [], {}
for i in range(1,int(1000/3)+1):#最短边
    for j in range(i,int(1000/2)):#中间边
        leng = (i**2+j**2)**0.5
        if leng % 1==0:
            sum = i+j+leng
            if  sum <= 1000:
                anfan.append(int(sum))
                try:
                    exdict[int(sum)].append([i, j, leng])
                except KeyError:
                    exdict[int(sum)] = [[i, j, leng]]
an,fan=0,0
for i in anfan:
    af=anfan.count(i)
    if an<=af:#选择出现最多的数值
        an=af
        fan=i
print(fan)
print(exdict[fan])
#答案：840。 有8个解，分别是：
#[40, 399, 401.0], [56, 390, 394.0], [105, 360, 375.0], [120, 350, 370.0], [140, 336, 364.0], [168, 315, 357.0], [210, 280, 350.0], [240, 252, 348.0]
