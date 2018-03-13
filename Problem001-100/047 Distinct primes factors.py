#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem047 Distinct primes factors

def an_pri(nu):#判断素数
    if nu==2:
        return True
    else:
        for i in range(2,int(nu**0.5)+1):
            if nu%i==0:
                return False
        return True
def an_com(numb):#判断一个数有几个不同的质因数
    fu=[]
    if an_pri(numb):
        fu.append(numb)
        return 1
    else:
        while not an_pri(numb):
            for i in range(2,int(numb**0.5)+1):
                if numb%i==0 and an_pri(i)  :
                    fu.append(i)
                    numb/=i
                    if an_pri(numb):
                        fu.append(int(numb))
                        break
        return len(set(fu))
n=2
while True:
    if an_com(n)!=4:
        n+=1
    else:
        if an_com(n+1)!=4:
            n+=2
        else:
            if an_com(n+2)!=4:
                n+=3
            else:
                if an_com(n+3)!=4:
                    n+=4
                else:
                    print(n)
                    break
#答案：134043
