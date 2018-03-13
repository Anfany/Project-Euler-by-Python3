#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem044 Pentagon numbers

def an_pan(number):#判断是否为五边形数
    if ((24*number+1)**0.5+1)%6==0:
        return True
an_set,i,af=set(),0,1
while af!=0:
    i+=1
    fan=int(i*(3*i-1)/2)
    an_set.add(fan)
    for an in an_set:
        if fan-an in an_set and an_pan(an+fan):
            print(fan, an, fan-an)
            af=0
#答案：五边形数对【7042750 ，1560090】
#差为：5482660
