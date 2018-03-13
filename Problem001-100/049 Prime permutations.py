#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem049 Prime permutations

def an_pri(nu):#判断素数
    if nu==2:
        return True
    else:
        for i in range(2,int(nu**0.5)+1):
            if nu%i==0:
                return False
        return True
anfan=[i for i in range(10**3,10**4) if an_pri(i)]#四位数中的素数
hu=0
for i in range(len(anfan)):
    a=anfan[i]
    for j in range(i+1,len(anfan)):
        b=anfan[j]
        if an_pri((a+b)/2) and (a+b)%2==0:#保证为等差序列
            if sorted(list(str(a)))==sorted(list(str(b))):#判断数字重排
                if sorted(list(str(a)))==sorted(list(str(int((a+b)/2)))):#判断数字重排
                    if a!=1487:
                        print(str(a)+str(int((a+b)/2))+str(b))
                        hu=1
    if hu==1:
        break
#答案：三个数分别为：2969，6299，9629
#最终结果：296962999629
