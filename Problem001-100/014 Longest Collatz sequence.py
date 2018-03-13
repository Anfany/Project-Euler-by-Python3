#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem014 Longest Collatz sequence

an_dict={1:1}
def an_collatz(number):
    if not an_dict.get(number,0):
        if number%2:
            an_dict[number]=an_collatz(3*number+1)+1
        else:
            an_dict[number]=an_collatz(number/2)+1
    return an_dict[number]
an,fan=0,0
for i in range(1,1000000):
    an_fan=an_collatz(i)
    if an_fan>an:
        an,fan=an_fan,i
print(fan)
#答案：837799
