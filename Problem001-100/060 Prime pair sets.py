#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem060 Prime pair sets

# 判断素数
def an_prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0 and number > i:
            return False
    return True

# 判断组合是否为素数
def Combine(listex):
    for i in range(len(listex) - 1):
        for j in range(i + 1, len(listex)):
            if not an_prime(int(str(listex[i]) + str(listex[j]))) or not \
                    an_prime(int(str(listex[j]) + str(listex[i]))):
                return False
    return True

# 得到nunm以内的素数集合
def PrimeSet(nunm):
    anset = []
    fan = 3
    while fan < nunm:
        if an_prime(fan):
            anset.append(fan)
        fan += 1
    return anset

# 暴力搜索函数
def Violence(num):
    dd = PrimeSet(num)
    for jj in range(len(dd)):
        for ii in range(jj + 1, len(dd)):
            if Combine([dd[ii], dd[jj]]):
                for gg in range(ii + 1, len(dd)):
                    if Combine([dd[ii], dd[gg], dd[jj]]):
                        for hh in range(gg + 1, len(dd)):
                            if Combine([dd[ii], dd[hh], dd[gg], dd[jj]]):
                                for cc in range(hh + 1, len(dd)):
                                    if Combine([dd[ii], dd[cc], dd[gg], dd[hh], dd[jj]]):
                                        return [dd[ii], dd[jj], dd[gg], dd[hh], dd[cc]]


primelist = Violence(10000)
print(primelist)
print(sum(primelist))
#答案：满足条件的一组素数：[5197, 13, 5701, 6733, 8389]
#和为：26033
