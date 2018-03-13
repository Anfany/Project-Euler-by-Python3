#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem046 Goldbach's other conjecture

def an_pri(nu):#判断素数
    if nu==2:
        return True
    else:
        for i in range(2,int(nu**0.5)+1):
            if nu%i==0:
                return False
        return True
an=7
while True:
    an+=2
    if not an_pri(an):#合数
        if all((((an-i)/2)**0.5)%1!=0 for i in range(2,an-1) if an_pri(i)):#寻找解
            print(an)#如果没有解，则输出
            break
#答案：5777
