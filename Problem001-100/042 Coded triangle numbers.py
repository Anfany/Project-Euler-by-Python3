#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem042 Coded triangle numbers

#读取文件
with open(r'C:\Users\GWT9\Desktop\p042_words.txt')as an_file:
    fan=an_file.read()
    fan_an=fan.replace('"','').split(',')
#判断是否为三角形数
def an_trin(number):
    sboot = int((2*number)**0.5)
    if 2*number==sboot*(sboot+1):
        return True
#计算单词中字母对应的顺序之和
def an_ord(str1):
    return sum(ord(i)-64 for i in str1)
fan=0
for h in fan_an:
    if an_trin(an_ord(h)):
        fan+=1
print(fan)
#答案：162
