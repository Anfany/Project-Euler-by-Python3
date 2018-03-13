#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem055 Lychrel numbers

def JudgeP(number):#判断回文数
    stnu = str(number)
    for i in range(int(len(stnu) / 2)):
        if stnu[i] != stnu[-i - 1]:
            return False
    return True
def Lcyder(number, nu=50):#50次之内变不成回文数
    d = nu
    while d > 0:
        number += int(str(number)[::-1])
        if JudgeP(number):
            return True
        else:
            d -= 1
    return False
d = 0
for i in range(10000):
    if not Lcyder(i):
        d += 1
print(d)
#答案：249
