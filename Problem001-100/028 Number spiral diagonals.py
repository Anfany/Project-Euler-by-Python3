#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem028 Number spiral diagonals

anfan=sum((j**2+j**2-3*(j-1))*2 for j in range(3,1002) if j%2==1)+1
print(anfan)
#答案：669171001
