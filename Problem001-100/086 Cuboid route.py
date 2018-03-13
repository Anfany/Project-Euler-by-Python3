#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem086 Cuboid route

import math
length = 3
count = 0
sign = 0
while 1:
    for jj in range(3, 2 * length):#[a, 1, 1],[a, a, a]均不可能
        boot = (jj ** 2 + length ** 2) ** 0.5
        if int(boot) - boot == 0:#判断最短距离恰好是整数
            if jj > length:
                count += length - math.ceil(jj / 2) + 1
            elif jj < length:
                count += int(jj / 2)
            #不会存在相等的情况
            if count > 1000000:
                sign = 1
                break
        if sign == 1:
            break
    if sign == 1:
        break
    else:
        length += 1
print(length)
#答案：1818
