#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem091 Right triangles with integer coordinates

#方法一：直接方法，判断三点是否组成直角三角形
Plist = [[x, y] for x in range(51) for y in range(51)]
Qlist = Plist.copy()

def judge(elist, xlist):
    one = (elist[0] - xlist[0]) ** 2 + (elist[1] - xlist[1]) ** 2
    two = (elist[0]) ** 2 + (elist[1]) ** 2
    three = (xlist[0]) ** 2 + (xlist[1]) ** 2
    blist = [one, two, three]
    if 0 in blist:
        return False
    else:
        if max(blist) * 2 == sum(blist):
            return True
        else:
            return False
count = 0
for jjj in Plist:
    for hhh in Qlist:
        if judge(jjj, hhh):
            count += 1
print(int(count * 0.5))

#方法二：根据几何知识，互相垂直的直线斜率乘积为-1**
def Euclidean(a, b):#计算最大公因数，辗转相除法
    d = a % b
    if d == 0:
        return b
    else:
        while d != 0:
            a, b = b, a % b
            d = a % b
        return b
count= 0
for i in range(1, 51):
    for j in range(1, 51):
        k = Euclidean(i, j)
        count += min(int((50 - i) * k / j), int((j * k / i))) * 2
count += 50 * 50 * 3#在边上的
print(count)
#答案：14234
