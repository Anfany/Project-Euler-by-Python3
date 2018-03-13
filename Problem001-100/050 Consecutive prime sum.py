#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem050 Consecutive prime sum

def an_pri(nu):#判断素数
    if nu==2:
        return True
    else:
        for i in range(2,int(nu**0.5)+1):
            if nu%i==0:
                return False
        return True
anfan=[i for i in range(2,5*10**3) if an_pri(i)]#素数集合
large,fanan,n,an_sum,an_num,an_prime,an_pri_num=0,0,2,0,0,0,0
while True:
    for i in range(n,len(anfan)):#连续的素数相加，如果不是往后推一位[n + 1]，继续。
        an_sum+=anfan[i]#连续素数的和
        an_num+=1#素数的个数
        if an_sum<10**6 and an_pri(an_sum):
            an_prime,an_pri_num=an_sum,an_num
        elif an_sum>10**6:
            n+=1
            an_sum=0
            break
    if fanan<an_pri_num:#判断个数最多的
        fanan,large=an_pri_num,an_prime
    if sum(i for i in anfan[n:fanan])>10**6:
        break
print(large)
#答案：997651
