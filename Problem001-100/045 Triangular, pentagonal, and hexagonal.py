#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem045 Triangular, pentagonal, and hexagonal

def an_fan(num):
    if((24*num+1)**0.5+1)%6==0:#判断五边形数
        if ((8*num+1)**0.5+1)%4==0:#判断六角形数
            return True
n=285
while True:
    n+=1
    fan=int(n*(n+1)/2)#三角形数
    if an_fan(fan):
        print(fan)
        break
#答案：1533776805
