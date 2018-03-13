#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem057 Square root convergents

#第一次迭代的初始值
a=2#分母
b=3#分子
er=0#记录代数
count=0#记录超过的次数
while er<1000:
    a,b=a+b,2*a+b#迭代表达式
    if (len(str(b)))>len(str(a)):
        count+=1
    er+=1
print(count)
#答案：153
