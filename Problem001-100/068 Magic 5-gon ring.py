#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem068 Magic 5-gon ring

import itertools as it
import numpy as np
#判断共享的数字集合
def magic(n):
    #数字列表
    select = list(range(1, 2*n + 1))
    #可能的数组列表
    plist = []
    #返回n个数字的组合
    for ii in it.combinations(select,n):
        if sum(list(ii)) % n == 0:#共同的数字之和必须能被n整除
            plist.append(list(ii))
    return plist

def comadd(exlist):
    #原始组合
    yuanshi = np.array(exlist)
    after = np.array(exlist[1:]+[exlist[0]])
    #关系字典
    save = {}
    for ii in range(len(yuanshi)):
        save[yuanshi[ii] +after[ii]] = [yuanshi[ii], after[ii]]
    return save

def judge(exlist):
    #去差集
    cha = list(set(list(range(1, 2 * len(exlist) + 1))).difference(set(exlist)))
    #计算exlist的可能的组合,
    problist = []
    pailie = it.permutations(exlist[1:], len(exlist) - 1)
    for i in pailie:
        if list(i)[::-1] not in problist:#去除掉组合重复的
            problist.append(list(i))
    #存储的字典
    savedict = {}
    for hh in problist:
        hh.insert(0, exlist[0])
        sadict = comadd(hh)
        if len(sadict.keys()) == len(cha):#如果字典长度不够，说明存在数字和相同的情况，去掉这种情形
            # 计算problist中的每一个组合是否满足条件
            sumlist = list(np.array(sorted(list(sadict.keys()))) + np.array(sorted(cha, reverse = True)))
            if len(set(sumlist)) == 1:
                savedict[tuple(cha)] = sadict
    return savedict

#定义输出数字序列的函数
def Transnum(exdict, keynum, weizhi, emptylist, keylist, sumdi):
    emptylist += str(sumdi - keynum) + str(exdict[keynum][weizhi]) + str( exdict[keynum][weizhi - 1]) + ','
    #选取键序列中的最小值
    keylist.append(keynum)
    for jj in exdict:
        if jj not in keylist:
            if exdict[keynum][weizhi - 1] == exdict[jj][weizhi]:
                keynum = jj
                return Transnum(exdict, keynum, weizhi, emptylist, keylist, sumdi)
    return emptylist

#输出所有的可能性
savelist = []
for idi in magic(5):
    #字典
    ddict = judge(idi)
    if len(ddict) != 0:
        #键中的最小值
        keynu = min(list(list(ddict.keys())[0]))
        #值中键的最大值
        numley = max(list(list(ddict.values())[0].keys()))
        for idd in [0, 1]:
            numstr = Transnum(list(ddict.values())[0], numley, idd, '', [], keynu + numley)
            savelist.append(numstr)
            print('%s: %s'%(keynu + numley, numstr))

#判断16数字最大的
lastnumber = 0
for j in savelist:
    #去掉逗号
    dele = j.replace(',','')
    if len(dele) == 16:
        #获得数字
        if lastnumber < int(dele):
            lastnumber = int(dele)
print(lastnumber)
#答案：
#所有“魔力”五边形环：
#14: 635,752,824,941,1013,
#14: 653,1031,914,842,725,
#16: 2410,5101,817,673,934,
#16: 2104,943,637,871,5110,
#16: 259,493,637,871,1015,
#16: 295,1051,817,673,439,
#17: 278,584,3410,6101,917,
#17: 287,971,6110,3104,548,
#17: 1610,3104,548,782,926,
#17: 1106,962,728,584,3410,
#19: 1810,2107,379,496,568,
#19: 1108,586,469,397,2710,
#最大的16位数字串是：6531031914842725
