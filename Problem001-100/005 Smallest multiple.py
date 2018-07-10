# !/usr/bin/python3.5
# -*- coding: UTF-8 -*-
# Author: AnFany


# Problem005 Smallest multiple


def an_decompose(num):  # 将一个数分解为素因数乘积
    arr = []
    ifg = 2
    while num != 1:
        if num % ifg == 0:
            while num % ifg == 0:
                arr.append(ifg)
                num /= ifg
        ifg = ifg + 1
    return arr


an = []  # 20以内的数分解为质因数
for i in range(2, 21):
    for w in an_decompose(i):
        an.append(w)


def an_list(list1, list2):
    for ity in list2:
        while list1.count(ity) < list2.count(ity):
            list1.append(ity)
    return list1

an = list(set(an))
fan = 2
while fan <= 20:  # 如果一个数的全部质因数包括在an里，则不增加。否则少几个加几个。
    an = an_list(an, an_decompose(fan))
    fan += 1

fan = 1  # 计算最终的乘积
for i in an:
    fan *= i
print(fan)
#答案：232792560
