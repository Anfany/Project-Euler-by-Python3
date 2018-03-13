#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem085 Counting rectangles

import numpy as np
i = 1
sanp = np.zeros((3000, 3000))#存储个数
start = 1
num = 100000
sign = 0
while 1:
    for j in range(1, start + 1):
        sanp[i, j] = sanp[j, i] = sanp[i - 1, j] + sanp[i, j - 1] - sanp[i - 1, j - 1] + i * j#动态规划方法
        #计算最小的差值
        result = abs(2e6 - sanp[i, j])
        if num > result:
            num = result
            re =[i, j].copy()
        if j == 1 and sanp[i, j] > 2e6:
            sign = -1
            break
        if sanp[i, j] > 2e6:
            sign = 1
            start = j
    if sign != 1:
        start += 1
    if sign == -1:
        break
    i += 1
print(re[0] * re[1])
#答案：2772
