#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


#一般方法：全部数字都遍历 用时：23.517s
def an_prime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0 and number!=i:
            return False
    return True
anfan=0
for i in range(2,2000000):#全部遍历
    if an_prime(i):
        anfan+=i
print(anfan)

#优化方法：数字筛选 用时：0.124s
def primes(n):
    an=[True]*n
    for i in range(3,int(n**0.5)+1,2):#消去合数
        if an[i]:
            an[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    primelist=[2]+[j for j in range(3,n,2) if an[j]]
    return sum(primelist)
print(primes(2000000))
