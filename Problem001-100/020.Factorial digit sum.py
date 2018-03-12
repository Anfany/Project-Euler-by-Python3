#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


def an_product(n):#计算阶乘
    nu=1
    for i in list(range(1,n+1)):
        nu*=i
    return nu
print(sum(int(i) for i in str(an_product(100))))
