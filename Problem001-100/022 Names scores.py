#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem022 Names scores

with open(r'C:\Users\GWT9\Desktop\secries11.txt')as an_file:#读取姓名数据
    fan=an_file.read()
    fan_an= sorted(fan.replace('"', '').split(','))#姓名排序
def fan_sumq(stit):#计算姓名的字母的和值
    return sum(ord(i)-64 for i in stit)
print(sum(fan_sumq(fan_an[i])*(i+1) for i in range(0,len(fan_an))))
#答案： 871198282
