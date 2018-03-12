#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany

#动态规划的思想解决
#可参见：http://www.jianshu.com/p/558294dae12e
import copy#引入复制的包
#读取数据
fan=open(r'C:\Users\GWT9\Desktop\secries.txt')
an=[]#存储数据
weizhi=[]#存储位置，用于记录经过的数字的坐标
for i in range(15):
    an.append([])
    weizhi.append([])
    x=fan.readline()
    for j in range(15):
        try:
            an[i].append(int(x[j*3:(j*3)+2]))
            weizhi[i].append([[i,j]])
        except ValueError:
            pass
fan.close()
copyan=copy.deepcopy(an)#深度复制，记录经过的数字需要用到
#根据值得大小取坐标的函数
def GetCoordinate(shuzu,hang,lie):
    if shuzu[hang][lie]>shuzu[hang][lie+1]:
        return [hang,lie]
    else:
        return [hang,lie+1]
#开始计算
for ii in range(len(an)-2,-1,-1):
    for j in range(len(an[ii])):
        ff=GetCoordinate(an,ii+1,j)
        weizhi[ii][j]+=[weizhi[ff[0]][ff[1]]][0]#添加数字比较大的坐标  
        an[ii][j]=max(an[ii+1][j],an[ii+1][j+1])+an[ii][j]#选择数字和比较大的路径

record=[]#根据记录的坐标，选择数字
for ii in weizhi[0][0]:
    record.append(copyan[ii[0]][ii[1]])
print(record)#经过的数字列表，从顶端开始
#[75, 64, 82, 87, 82, 75, 73, 28, 83, 32, 91, 78, 58, 73, 93]
#最大的路径和
print(an[0][0])

