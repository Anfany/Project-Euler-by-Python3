#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem076 Counting summations

def DP_Com(exlist,num):
    an=[1]+[0]*num
    for i in exlist :
        for j in range(i,num+1):
            an[j]+=an[j-i]
    return an[num]
print(DP_Com(list(range(1, 100)),100))
#答案：190569291
