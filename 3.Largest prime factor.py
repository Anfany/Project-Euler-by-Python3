#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany

def an_prime(number):#判断是否为素数
    if number==1 or number==2:
        return False
    for i in range(2,int(number**0.5)+1):#一个数的最大因数不超过其平方根
        if number%i==0:
            return False
    return True
an=0
for i in range(2,int(600851475143**0.5)):
    if 600851475143%i==0 and an_prime(i):
       if an<i:
          an=i
print(an)

