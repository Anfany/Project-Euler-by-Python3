#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem023 Non-abundant sums

def fan_sum(number):#判断是否是盈数
    hu=[1]
    for i in range(2,int(number**0.5)+1):
        if number%i==0 and number>i:
            hu.append(i)
            if number!=i**2:
                hu.append(number/i)
    if sum(i for i in hu)>number:
        return True
    
def an_sum(number):
    an,fan=set(),0
    for i in range(1,number+1):
        if fan_sum(i):
            an.add(i)
        if not any((i-j) in an for j in an):#判断是否可以写成两个盈数的和
            fan+=i
    return fan
print(an_sum(28123))
#答案：4179871
