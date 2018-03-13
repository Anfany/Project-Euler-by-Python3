#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem021 Amicable numbers

def fan_sum(number):#计算真因数的和
    hu=[1]
    for i in range(2,int(number**0.5)+1):
        if number%i==0 and number>i:
            hu.append(i)
            if number!=i**2:
                hu.append(number/i)
    return sum(f for f in hu)
an_dict={}
for i in range(1,10001):
    an_dict[i]=fan_sum(i)#存储真因数和的字典

fan=0
for i in range(1,10001):    
    try:
        if an_dict[an_dict[i]]==i and an_dict[i]!=i:#寻找d[a]=b and d[b]= a
            fan+=i
    except KeyError:
        pass
print(fan)
#答案：31626
