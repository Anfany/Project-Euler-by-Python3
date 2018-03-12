#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany

def an_prime(number):
    if number==1 or number==0:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0 and number>i:
            return False
    return True
d,count=0,0
while 1:
    if an_prime(d):
        count+=1
        if count==10001:
            break
    d+=1
print(d) 
