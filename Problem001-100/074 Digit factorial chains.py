#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem074 Digit factorial chains

stdict = {0: 1}#数字阶乘字典
start = 1
while start < 10:
    stdict[start] = start * stdict[start - 1]
    start += 1
def transdigit(num, di = stdict):#数转化为数字阶乘之和
    strnum = str(num)
    st = 0
    for ii in strnum:
        st += di[int(ii)]
    return st
def duging(number):#数字阶乘之链
    fu =[]
    while number not in fu:
        fu.append(number)
        dd = transdigit(number)
        number = dd
    fu.append(number)
    return fu
result = {}
count = 0
for iii in range(999999, 0, -1):
    if iii not in result:
        nn = duging(iii)
        legn = len(nn)
        result[iii] = legn - 1
        if legn - 61 == 0:
            count += 1
        jwei = nn.index(nn[-1])
        for iij in range(1, legn - 1):
            if nn[iij] not in result:
                if iij < jwei:
                    result[nn[iij]] = legn - iij - 1
                else:
                    result[nn[iij]] = legn - jwei -1
            else:
               break
print(count)
#答案：402
