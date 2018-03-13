#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem030 Digit fifth powers

def an_fan(number):
    an_fan=[]
    for i in range(len(str(number))):
        an_fan.append(str(number)[i])
    if sum(int(i)**5 for i in an_fan)==number:
        return True
fanlist = [i for i in range(2,9**6) if an_fan(i)]
print(fanlist)
print(sum(fanlist))
#答案：[4150, 4151, 54748, 92727, 93084, 194979]，和为443839
