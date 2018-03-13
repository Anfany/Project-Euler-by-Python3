#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem025 1000-digit Fibonacci number

def an_fib(num):
    an,fan,an_fan=1,1,2
    while len(str(fan))<num:#判断位数
        an_fan+=1
        an,fan=fan,an+fan#斐波那契序列
    return an_fan
print(an_fib(1000))
#答案：4782
