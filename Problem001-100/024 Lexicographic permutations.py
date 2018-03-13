#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem024 Lexicographic permutations

#思路：100万=a*9!+b*8!+……+k*0!
def an_pro(num):#计算阶乘
    if num==0:
        return 1
    else:
        nu=1
        while num>0:
            nu*=num
            num-=1
        return nu
#计算每个阶乘前面的数字的位置编号
def fan_lis(number):#number=100万,count=10,lis存储过程中的数字
    anlist=[]#存储过程中的数字
    digitcount=9
    while number>=0:
        jiecheng=an_pro(digitcount)#计算count个数字的全排列组成的数字个数
        ji=int(number/jiecheng)#计算阶乘倍数
        anlist.append(ji)#存储
        nu=ji*jiecheng
        number-=nu
        digitcount-=1
        if digitcount==0:
            break
    anlist.append(0)
    return anlist
fan=fan_lis(999999)#第100万位的数字
#将上面程序的位置编号转化为对应的数字
fanfan=list(range(0,10))
fan_an=[]#存储对应的数字
for i in range(0,len(fan)):
    fan_an.append(fanfan[fan[i]])
    fanfan.remove(fanfan[fan[i]])
#输出最终的数字  
an_str=''
for i in fan_an:
    an_str+=str(i)#最终输出数字
print(an_str)
#答案：2783915460
