#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem002 Even Fibonacci numbers

a,b=1,2
fan=2#开始的两项中的偶数
while a+b<=4000000:
    a,b=b,a+b
    if(a+b)%2==0:#只计算偶数
        fan+=a+b
print(fan)
#答案：4613732
