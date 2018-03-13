#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem062 Cubic permutations

#将数转化为重排后的最大值
def NumToStr(number):
    lists=sorted(list(str(number)),reverse=True)
    strs=''.join(lists)
    return strs
#开始计算
exdict={}
long=[]
num=1
while len(long)<6:
    sf=NumToStr(int(num**3))
    if  sf in exdict:
        exdict[sf].append(num)
    else:
        exdict[sf]=[num]
    long=max(exdict.items(),key=lambda x:len(x[1]))[1]
    num+=1
    if len(long)==5:#如果有5个了，在退出循环
        for ggg in long:
            print('%d^3 = %d'%(ggg, ggg ** 3))
        print('最小的数：%d'%(long[0]**3))
        break
#答案：五个数分别是：
#5027^3 = 127035954683
#7061^3 = 352045367981
#7202^3 = 373559126408
#8288^3 = 569310543872
#8384^3 = 589323567104
#最小的数：127035954683
