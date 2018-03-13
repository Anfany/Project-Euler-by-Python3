#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem100 Arranged probability

#blue:b, total:t
#2b(b-1)=t(t-1)==>8b^2-8b+1=(2t-1)^2
#pell's Equation2u^2-1=d^2==>2(2b-1)^2-1=(2t-1)^2
#d=2t-1,u=2b-1. t=(d+1)/2, b=(1+u)/2
#pell's Equation==>d^2-2u^2=-1
#初始解
d = 1
u = 1
minnumber = 1e12

while 1:
    if (d + 1) / 2 > minnumber:
        print(int((u + 1) / 2))
        break
    d, u = 3 * d + 4 * u, 2 * d + 3 * u
    print('Total:%d, blue:%d'%((d + 1) / 2, (u + 1) / 2))
##运行结果
#Total:4, blue:3
#Total:21, blue:15
#Total:120, blue:85
#Total:697, blue:493
#Total:4060, blue:2871
#Total:23661, blue:16731
#Total:137904, blue:97513
#Total:803761, blue:568345
#Total:4684660, blue:3312555
#Total:27304197, blue:19306983
#Total:159140520, blue:112529341
#Total:927538921, blue:655869061
#Total:5406093004, blue:3822685023
#Total:31509019101, blue:22280241075
#Total:183648021600, blue:129858761425
#Total:1070379110497, blue:756872327473
#答案：756872327473
