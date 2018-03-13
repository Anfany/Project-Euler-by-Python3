#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem035 Circular primes

def an_del(number):#删除具有某些特征的数
    ji=list(str(number))
    su,us=[0,2,4,6,8,5],[4,6,8,9]
    if len(ji)==1:#不是素数
        if number in us:
            return True
    else:
        for i in ji:#以su中数字结尾的都不是素数
            if int(i) in su:
                return True
        return False

def com_pri(number):#判断素数
    if number==2:
        return True
    else:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                return False
        else:
            return True
def an_fan(number):#将一个数循环
    hu=list(str(number))
    huuu=[hu]
    for i in range(1,len(hu)):
        a=[0]*len(hu)
        for h in range(len(hu)):
            if i+h>=len(hu):
                a[h]=hu[i+h-len(hu)]
            else:
                a[h]=hu[i+h]
        huuu.append(a)
    nu_hu=[]
    for jj in range(len(huuu)):
        nnu=''
        for hh in range(len(huuu[0])):
            nnu+=huuu[jj][hh]
        nu_hu.append(int(nnu))
    return nu_hu

anfan=0
for i in range(2,1000000):
    if not an_del(i) and com_pri(i):
        hh=0
        for hg in an_fan(i):
            if not com_pri(hg):
                hh = 1
                break
        if hh==0:
            anfan+=1
print(anfan)
#答案：55
