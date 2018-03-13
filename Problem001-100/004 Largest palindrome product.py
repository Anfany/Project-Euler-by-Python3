#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem004 Largest palindrome product

def an_palindromic(number):#判断回文数
    an=[i for i in str(number)]
    fan=0
    for i in range(len(an)):
        if an[i]==an[len(an)-1-i]:
            fan+=1
    if fan==len(an):
        return True     
an=[]   
for i in range(100,1000):
    for j in range(100,1000):
        if an_palindromic(i*j):
            an.append(i*j)
print(max(an))
#答案：993*913=906609
