#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem033 Digit cancelling fractions

def an(li1,li2):#判断去除共同数字后的剩余数字
    for i in li1:
        if i not in li2:
            return int(i)
def fan(n1,n2):#计算n1,n2约分后n2的值
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            n1//=i
            n2//=i
    return n2
def anfan(n1,n2):#判断2个数是否有共同的数字
    a,b=list(str(n1)),list(str(n2))
    if len(a+b)==len(set(a+b))+1 and '0' not in a and '0' not in b:
        return True
def fanan(n1,n2):#判断两个数去除掉共同的数字之后的商和之前商是否相等
    a,b=list(str(n1)),list(str(n2))
    c=a+b
    a1,b1=an(c,b),an(c,a)
    if n1/n2==a1/b1:
        return True
fan_an,an_fan=1,1
for i in range(10,100):
    for j in range(i,100):
        if anfan(i,j) and fanan(i,j):
            xa,xb=list(str(i)),list(str(j))
            xc=xa+xb
            print('%d / %d = %d / %d'%(i, j, an(xc,xb), an(xc,xa)))
            fan_an*=an(xc,xa)
            an_fan*=an(xc,xb)
print(fan(an_fan,fan_an))
#答案：四个非平凡分数：
#16 / 64 = 1 / 4
#19 / 95 = 1 / 5
#26 / 65 = 2 / 5
#49 / 98 = 4 / 8
#分数乘积约分后的分母：100
