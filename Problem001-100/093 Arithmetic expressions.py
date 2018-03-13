#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem093 Arithmetic expressions

import itertools
operator = ['+', '-', '*', '/']
#只存在五种结构
format = ['((%d%s%d)%s%d)%s%d', \
          '(%d%s%d)%s(%d%s%d)', \
          '(%d%s(%d%s%d))%s%d', \
          '%d%s((%d%s%d)%s%d)', \
          '%d%s(%d%s(%d%s%d))']
#数字和字母穿插
def Chuan(num, letter):
    chuan = []
    for jj in range(len(num)):
        chuan.append(num[jj])
        try:
            chuan.append(letter[jj])
        except IndexError:
            pass
    return chuan

#构建数字和算子的组合
def Combine(numlist, target, oplist = operator, form = format):
    expre = []
    for jj in list(itertools.permutations(numlist, len(numlist))):#数字
        for ii in list(itertools.product(oplist, repeat = 3)):#算子
            fu = Chuan(list(jj), list(ii))#交叉
            for ff in form:#遍历每一种情况
                try:
                    if eval(str(ff)%tuple(fu)) == target:
                        return True
                except ZeroDivisionError:
                    pass
    return False

n  = 0
for a  in range(1, 7):
    for b in range(a + 1, 8):
        for c in range(b + 1, 9):
            for d in range(c + 1, 10):
                tar = 1
                while Combine([a, b, c, d], tar):
                    tar += 1
                if n < tar:
                    cc = '%s%s%s%s'%(a,b,c,d)
                    n = tar
                if tar == 1:
                    break
print(cc)
#答案：1258
