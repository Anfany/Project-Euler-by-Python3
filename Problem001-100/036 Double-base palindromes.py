#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem036 Double-base palindromes

def an_fan(strr):#判断回文数
    if str(strr) == str(strr)[::-1]:
        return True
    else:
        return 0
def an_bin(n):#转为二进制
    if n==0:
        return '0'
    list_bian=''
    while n>=1:
        if n%2==0:
            list_bian+='0'
        else:
            list_bian+='1'
        n=int(n/2)
    return list_bian[::-1]
anfan=0
for i in range(1,1000000):
    if an_fan(str(i)) and an_fan(an_bin(i)):
        anfan+=i
print(anfan)
#答案：872187
