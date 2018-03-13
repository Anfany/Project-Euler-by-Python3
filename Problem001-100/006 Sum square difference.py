#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem006 Sum square difference

an=sum(i**2 for i in range(1,101))
fan=sum(i for i in range(1,101))**2
print(fan-an)
#答案：25164150
