#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem064 Odd period square roots

#定义函数
def Get(number):
    #计算平方根
    dd=number**0.5
    #取整，确定开始值
    start=int(dd)
    #存储值、和周期值
    peilist=[[start],[]]
    #存储每一次的中间过程
    middle=[]
    #第一个中间过程
    fenzi=1
    sfenmu=number
    sign=-start
    first=[fenzi,sfenmu,sign]
    while first not in middle:
        middle.append(first)
        hhd=middle[-1][1]-middle[-1][2]**2#分母
        #分子总系数
        fenziall=middle[-1][0]*(start-middle[-1][2])
        #值
        num=int(fenziall/hhd)
        peilist[-1].append(num)
        #周期值
        fenzi=int(hhd/middle[-1][0])
        sfenmu=number
        sign=int((-middle[-1][2])-fenzi*num)
        first=[fenzi,sfenmu,sign]
    return number,peilist #返回值和周期值
#开始计算
count=0
for i in range(1,10001):
    ss=i**0.5
    if int(ss)-ss!=0:
        dd=Get(i)
        if len(dd[-1][-1])%2==1:
            count+=1
print(count)
#答案：1322
