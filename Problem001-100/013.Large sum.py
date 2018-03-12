#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany

def an_count(number):
    hu=0
    if number%(number**0.5)==0:
        for i in range(1,int(number**0.5)):
            if number%i==0:
                hu+=1
        return hu*2+1
    elif number%(int(number**0.5)+1)==0 :
        for i in range(1,int(number**0.5)+1):
            if number%i==0:
                hu+=1
        return hu*2+1
    else:
        for i in range(1,int(number**0.5)+1):
            if number%i==0:
                hu+=1
        return hu*2
an=1
fan=1
while an_count(fan)<=500:
    an+=1
    fan+=an
if an_count(fan-an)<500:
    print(fan)
else:
    print(fan-an)

