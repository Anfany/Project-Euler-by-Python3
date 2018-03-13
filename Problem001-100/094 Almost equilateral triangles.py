#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem094 Almost equilateral triangles

#Pell方程x^2 - 3y^2 = 1， 初始解为(2, 1)
x = 2
y = 1
summ = 0
while 1:
    ynum = 2 * y + 1 * x
    xnum = x * 2 + 3 * y * 1
    x = xnum
    y = ynum
    # 第一种(a, a+1, a+1)
    # 化为((3a+4)/2)^2-3h^2=1，利用Pell方程
    if 2 * xnum - 2 < 1e9:#周长限制
        if (2 * xnum - 4) / 3 % 2==0:#判断边长为整数
            squre = ynum * (xnum - 2) / 3
            if int(squre) - squre == 0:#面积为整数
                summ += 2 * xnum - 2
    else:
        break
    # 第二种(a, a-1, a-1)
    # 化为((3a-4)/2)^2-3h^2=1，利用Pell方程
    if 2 * xnum + 2 < 1e9:##周长限制
        if  (2 * xnum + 4) / 3 % 2==0:#判断边长为整数
            squre = ynum * (xnum + 2) / 3
            if int(squre) - squre == 0:##面积为整数
                summ += 2 * xnum + 2
    else:
        break
print(summ)
#答案：518408346
