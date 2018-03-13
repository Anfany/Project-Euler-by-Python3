#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem040 Champernowne's constant

allstr = ''
start = 1
cd = {}
while len(allstr) < 10 ** 6 + 1:
    allstr += str(start)
    start += 1
pro = 1
for ii in range(0, 7):
    number = int(int(allstr[10 ** ii - 1]))
    pro *=  number
    cd[int(10 ** ii)] = number
print(pro)
print(cd)
#答案：分别对应的数字为：{'d100000': 2, 'd100': 5, 'd1000000': 1, 'd10000': 7, 'd1': 1, 'd10': 1, 'd1000': 3}
#乘积为：210。
