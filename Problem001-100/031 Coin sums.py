#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem031 Coin sums

#动态规划思想，关于动态规划可参见：https://www.jianshu.com/p/e515efee2310
an=[1]+[0]*200
fan=[1,2,5,10,20,50,100,200]
for i in fan:
    for j in range(i,201):
        an[j]+=an[j-i]
print(an[200])
#答案：73682
