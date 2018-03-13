#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem099 Largest exponential

import math
fan=open(r'C:\Users\GWT9\Desktop\p099_base_exp.txt')#数据文件
#存储words的list
explist =[]
for i in fan:
    com = []
    for hh in i.split(','):
        com.append(int(hh))
    explist.append(com)
#转化为对数比较
sinum = 0
hang = 0
for num in explist:
    dlog = math.log(num[0]) * num[1]
    hang += 1
    if sinum < dlog:
        dnum = hang
        sinum = dlog
print(dnum)
#答案：709
