#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem041 Pandigital prime

#这个数字不可能是8、9位数。因为可以被3整除。
def an_pri(number):#判断素数
    if number==2:
        return True
    elif number>2:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                return False
        return True
    elif number==1:
        return False
def an_lastdi(number):#根据尾数筛选素数
    hu,hh=[2,4,6,8,5],list(str(number))
    if int(hh[-1]) in hu:
        return False
    return True
def an_len(number):#根据数字长度筛选素数
    uh=len(str(number))
    if uh==9 or uh==6 or uh==3:
        return False
    return True
def an_once(number):#判断全数字的
    hu=list(str(number))
    uh,an_hu=list(range(1,len(hu)+1)),[]
    for j in hu:
        an_hu.append(int(j))
    if sorted(an_hu)==uh:
        return True
for i in range(7654321,1,-1):
    if an_len(i) and an_lastdi(i) and an_once(i):
        if an_pri(i):
            print(i)
            break
#答案：7652413
