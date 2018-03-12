#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


def an_prime(number):#判断是否为质数
    for i in range(2,int(number**0.5)+1):
        if number%i==0 and number>i:
            return False
    return True
def an_decompose(number):#数分解为质因数的乘积
    an=[]
    while not an_prime(number):
        for i in range(2,int(number**0.5)+1):
            if number%i==0 and an_prime(i):
                an.append(i)
                number=int(number/i)
    if number!=1:
        an.append(number)
    return an
an=[]#20以内的数分解为质因数
for i in range(2,21):
    for w in an_decompose(i):   
        an.append(w)
def an_list(list1,list2):
    for i in list2:
        while list1.count(i)<list2.count(i):
            list1.append(i)
    return list1
an=list(set(an))
fan=2
while fan<=20:#如果一个数的全部质因数包括在an里，则不增加。否则少几个加几个。
    an=an_list(an,an_decompose(fan))
    fan+=1
fan=1#计算最终的乘积
for i in an:
    fan*=i
print(fan)
