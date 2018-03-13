#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem037 Truncatable primes

def an_fan(number):#含有偶数字的肯定不是双向可截短素数
    ab=[0,4,6,8]
    hu=str(number)
    for i in ab:
        if str(i) in hu:
            return False
    return True
def com_pri(number):#判断素数
    if number==2:
        return True
    elif number==1:
        return False
    else:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                return False
        return True
def fan_an(number):#将数左右依次截短
    hu=[]
    uh=str(number)
    if len(uh)==1:
        return [8]
    else:
        for i in range(len(uh)):
            hu.append(uh[i:])
            if uh[:i]!='':
                hu.append(uh[:i])
    return hu
m,h,b=0,10000,-1
number = []
while m<11:
    b+=1
    for i  in range(b*h,(b+1)*h):
        if an_fan(i) and com_pri(i):
            h2=1
            for j in fan_an(i):
                if not com_pri(int(j)):
                    h2*=0
            if h2==1:
                number.append(i)
                m+=1#满足条件的数的个数
print(number)
print(sum(number))
#答案：11个数分别是：[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]。
#和为748317
