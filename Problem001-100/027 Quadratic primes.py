#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem027 Quadratic primes

def com_pri(number):#判断素数
    if  number==2:
        return True
    else:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                return False
        return True
fan_an=[x for x in range(2,1001) if com_pri(x)]#n =0 时， b为素数
def an_fan(i,j,n, c=0):
    if com_pri(abs(n**2+i*n+j)):
         c+=1
         return an_fan(i,j,n+1,c)
    else:
         return c
number=0
for j in fan_an:
    for i in [x-j-1 for x in fan_an]:#n= 1 时， a+b+1 为素数
        result=an_fan(i,j,0,c=0)
        if number <= result:
            number = result
            ab = [j, i]
print(ab)
print(ab[0]*ab[1])
#答案：-59231
