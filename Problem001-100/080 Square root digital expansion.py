#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem080 Square root digital expansion

#方法一：利用python的小数精确库
import decimal#调用系统库
decimal.getcontext().prec = 120 #设置精度
result = 0
for i in range(1, 100):#前100个自然数0-99
    sq = i ** 0.5
    if sq - int(sq) != 0:#判断是不是完全平方数
        sboot = decimal.Decimal(i).sqrt()
        for jj in str(sboot)[: 101]:#前100位数字
            if jj != '.':
                result += int(jj)
print(result)
#方法二：利用Frazer Jarvis's method
def coms(n):#计算n的无理数平方根的前100位数字和
    result = ''
    a, b = 5 *n, 5
    while len(result) < 100:#前100位数字
        if a >= b:
            a, b = a - b, b + 10
        else:
            a, b = a * 100, 10 * b - 45
        result = str(b)[0 : -2]
    sumnum = 0
    for jj in result:
        sumnum += int(jj)
    return sumnum
lastnum = 0
for ii in range(1, 100):
    sq = ii ** 0.5
    if sq - int(sq) != 0:
        lastnum += coms(ii)
print(lastnum)
#答案：40886
