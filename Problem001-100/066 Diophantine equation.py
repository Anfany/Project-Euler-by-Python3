#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem066 Diophantine equation

#Pell方程解题思路
#由X^2-D*Y^2=1。可得根号D约等于X/Y。而根号D恰好可以变为连分数的形式
def GetPell(number):
    sboot=number**0.5
    #判断是否为完全平方数
    if int(sboot)-sboot==0:
        return [number]
    else:
        #开始计算根号D的连分数形式
        P=0
        Q=1
        a=int(sboot)
        #第0和第1个渐进分数
        p=[1,a]#分子
        q=[0,1]#分母
        while p[1]**2-number*(q[1]**2)!=1:
            #中间变量
            P=a*Q-P
            Q=(number-P**2)/Q
            a=int((int(sboot)+P)//Q)
            #渐进分数
            pp=a*p[1]+p[0]#分子
            qq=a*q[1]+q[0]#分母
            #存储
            p=[p[1],pp]
            q=[q[1],qq]
        return [p[1],number,q[1]]
#开始计算
x=0
d=0
for ipell in range(1001):
    result=GetPell(ipell)
    if len(result)==3:#排除完全平方的数
        if x<result[0]:#选择最小值
            x=result[0]
            d=result[1]
        elif x==result[0] and d<result[1]:#一样的X值，选择D最小的值
            d=result[1]
print(d)
#答案：661
