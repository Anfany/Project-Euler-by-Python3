#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem009 Special Pythagorean triplet

for i in range(1,300):#abc最小值肯定低于300
    for j in range(1,500):#abc中间值肯定低于500
        if i**2+j**2==(1000-i-j)**2:
            print(i,j,1000-i-j)#200 375 425
            print(i*j*(1000-i-j))
#答案：31875000
