#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem026 Reciprocal cycles

import re
from decimal import *
getcontext().prec,an_fan=1000*5 ,0
def an_match(number):
    fan_form=r"(\d+?)\1" #正则表达式匹配重复的数字
    an=re.search(fan_form, str(number))
    if an:
        return an.group(1)
def fan_num(aa):
    if len(str(int(aa)))>=1:
        return 10**(len(str(aa))-1)
    else:
        return 1

for i in range(1,1000):
    fan=[an_match(Decimal(1)*fan_num(i)/Decimal(i))]# 防止匹配的数字为0，因此分子要相应的扩大倍数，保证小数点后第一个数字不为0
    if fan!=[None]:#只有无限不循环的小数才进行判断
        if len(fan[0]) >= an_fan:# 选取最长的
            an_fan = len(fan[0])
            dnumber = i
print(dnumber)
#答案：983
