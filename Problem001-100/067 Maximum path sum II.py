#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem067 Maximum path sum II

#读取数据
fan=open(r'C:\Users\GWT9\Desktop\p067_triangle.txt')
an=[]
for i in range(100):
    an.append([])
    x=fan.readline()
    for j in range(100):
        try:
            an[i].append(int(x[j*3:(j*3)+2]))
        except ValueError:
            pass
fan.close()
#路径和最小动态规划
for ii in range(len(an)-2,-1,-1):
    for j in range(len(an[ii])):
        an[ii][j]=max(an[ii+1][j],an[ii+1][j+1])+an[ii][j]#动态规划思想
print(an[0][0])
#答案：7273
