#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem058 Spiral primes

def JudgePrime(number):#判断素数
    if number == 1:
        return False
    elif number == 2:
        return True
    for ip in range(2, int(number ** 0.5) + 1):
        if number % ip == 0:
            return False
    return True
def Judge(exlist):#判断素数的个数
    pcount = 0
    for ip in exlist:
        if JudgePrime(ip):
            pcount += 1
    return pcount

percent = 1
#利用start 和 per 得到增加的对角线数字
start = [1, 1, 1, 1]
per = [2, 4, 6, 8]
times = 1
primecount = 0
c = 1

while percent >= 0.1:
    exli = []#边长每增加2， 对角线元素增加的数字
    for j in range(len(start)):
        exli.append(start[j] + per[j])
    primecount += Judge(exli)#累积的素数个数
    percent = primecount / (1 + c * 4)#素数比例
    times += 2#边长
    c += 1
    start = exli.copy()
    for ia in range(len(per)):
        per[ia] += 8
print(times)
#答案：26241
