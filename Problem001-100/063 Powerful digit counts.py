#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem063 Powerful digit counts

#个数
count=0
#位数从1开始
weishu=1
while 1:
    low=10**(weishu-1)#几位数的下限
    up=10**weishu-1#几位数的上限
    sboot=low**(1/(weishu))#下限的方根
    #获得sboot与9之间的整数个数
    dd=9-int(sboot)
    if dd==0:
        print(count)
        break
    else:
        if int(sboot)-sboot==0:
            count+=dd+1
        else:
            count+=dd
    weishu+=1
#答案：49
