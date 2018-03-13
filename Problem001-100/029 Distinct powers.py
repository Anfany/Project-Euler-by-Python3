#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem029 Distinct powers

an=[]
fan=0
for i in range(2,101):
    for j in range(2,101):
        if i**j not in an:
            fan+=1
            an.append(i**j)
print(fan)
#答案：9183
