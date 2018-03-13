#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem051 Prime digit replacements

import itertools#引入组合库
def JudgePrime(num):#判断素数
    if num==1 or num==2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
def JuList(li):#判断替换的数字序列中素数的个数
    return [JudgePrime(i) for  i in li].count(True)
#判断要加的数
def Jadd(num,s='1'):
    #记录位置
    weizhi=[]
    fan=list(str(num))
    for i in fan[:-1]:#最后一位去除
        if i==s:
            t=fan.index(i)
            fan[fan.index(i)]='w'
            weizhi.append(len(fan)-t-1)
    #获得全排列
    du=[]
    for ig in range(len(weizhi)):
        for gi in list(itertools.combinations(weizhi,ig+1)):
            du.append(gi)
    #根据全排列后的确定加的数字
    shuzi=[]
    for j in du:
        sumsum=0
        for js in j:
            sumsum+=10**js
        shuzi.append(sumsum)
    return shuzi
#开始
bu=0
st=100000
while bu!=1:
    if JudgePrime(st):
        for iss in range(3):
            for iadd in Jadd(st,s=str(iss)):
                jjuu=[st]
                for ij in range(1,9-int(iss)+1):
                    jjuu.append(st+ij*iadd)
                if JuList(jjuu)==8:
                    print(st,iadd,jjuu)
                    bu=1
        st+=1
    else:
        st+=1
#答案：素数序列为：[121313, 222323, 323333, 424343, 525353, 626363, 727373, 828383, 929393]，第1，3，5位替换。
#最小的素数：121313。
