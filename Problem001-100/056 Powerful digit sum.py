#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem056 Powerful digit sum

sumb=0
for i in range(1,100):
    for j in range(1,100):
        d=sum([int(i) for i in list(str(i ** j))])
        if sumb<d:
            sumb=d
            dishu = i
            mi = j
print(dishu, mi)
print(sumb)
#答案：99^95， 数字和是972
