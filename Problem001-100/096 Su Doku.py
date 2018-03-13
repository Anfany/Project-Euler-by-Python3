#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem096 Su Doku

import numpy as np
fan=open(r'C:\Users\GWT9\Desktop\p096_sudoku.txt')#数据文件
an =[]
listfan = []
while 1:
    x = fan.readline()
    if len(x) == 0:
        break
    try:
        int(x)
        fanlist = []
        for jj in x:
            if jj != '\n':
                if jj == '0':
                    fanlist.append(np.nan)
                else:
                    fanlist.append(int(jj))
        listfan.append(fanlist)
    except ValueError:
        pass
    if len(listfan) == 9:
        an.append(listfan)
        listfan = []
fan.close()
#all problem data
an = np.array(an)

#sudoku
# 计算可能性
def ProbNumber(hang, lie, data):
    # 行数据
    H = list(data[hang])
    # 列数据
    L = list(data[:, lie])
    # 宫数据
    G = []
    sfang = int(len(data) ** 0.5)
    hh = hang // sfang
    ll = lie // sfang
    # 宫数据添加
    for ig in range(sfang):
        for gi in range(sfang):
            G.append(data[hh * sfang + ig, ll * sfang + gi])
    # 该点的可能性
    lal = list(H) + list(L) + G
    prob = [ip for ip in list(range(1, len(data) + 1)) if ip not \
            in lal]
    return prob

# 为数据中的空元素选择可能性字典
def ForK(data):
    Kdict = {}
    for ik in range(len(data)):
        for ki in range(len(data)):
            if np.isnan(data[ik, ki]):
                # 转换，便于字典的最下值是唯一的
                trans = ProbNumber(ik, ki, data)
                jieti = len(trans) * 10000000 + ik * 10000 + ki * 10
                Kdict['%s-%s' % (ik, ki)] = [jieti, len(trans), trans]
    return Kdict

# 选择可能性最小的位置
def SeleM(ddict):
    Small = min(ddict.items(), key=lambda x: (x[1][0]))[0]
    # 位置
    weizhi = Small.split('-')
    # hang
    Ha = int(weizhi[0])
    # lie
    Li = int(weizhi[1])
    # 集合
    SE = ddict[Small][2]
    return Ha, Li, SE

ss = 0
global NU
VAR_NAME = locals()
for ifrfr in range(len(an)):
    # 初始状态
    InitialState = {}
    InitialState[0] = an[ifrfr]
    # 取值字典
    NumDict = {}
    NU = 1
    # 状态转移
    # 记录栈中调用函数的次数
    minzhai = 0
    def TransFer(insta, numdi, n=0, c=minzhai):
        # 判断是否满足条件
        if len(ForK(insta[n])) == 0:
            global NU
            NU = 0
            return insta, numdi, n
        # 选择最小的
        mmi = SeleM(ForK(insta[n]))
        if c > 900:
            return insta, numdi, n

        if len(mmi[2]) == 0:
            del insta[n]
            c += 1
            return TransFer(insta, numdi, n - 1, c)
        else:
            middle = insta[n].copy()
            if n in numdi:
                if numdi[n] + 1 < len(mmi[2]):
                    numdi[n] += 1
                    middle[mmi[0], mmi[1]] = mmi[2][numdi[n]]
                    n += 1
                    insta[n] = middle.copy()
                    c += 1
                    return TransFer(insta, numdi, n, c)
                else:
                    del numdi[n]
                    del insta[n]
                    c += 1
                    return TransFer(insta, numdi, n - 1, c)
            else:
                numdi[n] = 0
                middle[mmi[0], mmi[1]] = mmi[2][0]
                n += 1
                insta[n] = middle.copy()
                c += 1
                return TransFer(insta, numdi, n, c)
    c_0 = TransFer(InitialState, NumDict)
    # 最终的函数
    def Sudoku():
        count = 1
        while NU != 0:
            VAR_NAME['c_%s' % count] = TransFer(eval('c_%s' % (count - 1))[0], eval('c_%s' % (count - 1))[1],
                                                eval('c_%s' % (count - 1))[2])
            count += 1
        dd = eval('c_%s' % (count - 1))[0][eval('c_%s' % (count - 1))[2]][0][:3]
        return dd
    ss += np.sum(Sudoku() * np.array([100, 10, 1]))#左上角三个数字连接起来
print(int(ss))
#答案：24702
