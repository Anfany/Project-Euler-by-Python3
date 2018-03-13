#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem084 Monopoly odds

import numpy as np
import random
#计算随机数
def Comnum(num, count):#计算几个几面色子的随机数
    numlist = []
    st = 0
    while st < count:
        numlist.append(random.randint(1, num))
        st += 1
    return numlist

#CH卡
chlist = list(np.array([0, 10, 11, 24, 39, 5, 99, 99, 999, 9999] +[99999] * 6)[random.sample(range(16), 16)])#99999代表无效牌，随即洗牌
chdict ={7: [15, 12], 22: [25, 28], 36: [5, 12]}
#CC卡
bxlist = list(np.array([0, 10] +[99999] * 14)[random.sample(range(16), 16)])#99999代表无效牌，随即洗牌
bxdict = [2, 17, 33]

#定义取卡放卡后的函数
def Card(exlist):
    return exlist[1:] + [exlist[0]]#取完牌，将牌放在最下面

#计数字典
countdict = {kk : 0 for kk in range(40)}#每个数字代表一个方格
#开始模拟
start = 0
jailsign = 0
monitimes = 10000#模拟的次数
for moni in range(monitimes):
    #开始随机数
    randomlist = Comnum(4, 2)#计算2个4面色子的随机数
    sezi = sum(randomlist)#计算前进的步数
    if randomlist[0] == randomlist[1]:
        jailsign += 1
    else:
        jailsign = 0
    if jailsign >= 3:#连续三次掷出相同的点数
        countdict[10] += 1#JAIL
        start = 10
    else:
        busu = (sezi + start) % 40
        if busu == 30:#G2J
            countdict[10] += 1#JAIL
            start = 10
        else:
            if busu in bxdict:#CC card
                if bxlist[0] == 99999:#Stop Moving
                    countdict[busu] += 1
                    start = busu
                else:
                    countdict[bxlist[0]] += 1
                    start = bxlist[0]
                bxlist = Card(bxlist).copy()
            elif busu in chdict:#CH card
                if chlist[0] == 99:#next R
                    nnum = chdict[busu][0]
                elif chlist[0] == 999:#next U
                    nnum = chdict[busu][1]
                elif chlist[0] == 99999:#Stop Moving
                    nnum = busu
                elif chlist[0] == 9999:#Backward 3
                    nnum = busu - 3
                    if nnum == 33:#CC card
                        if bxlist[0] != 99999:  # Stop Moving
                            nnum = bxlist[0]
                        bxlist = Card(bxlist).copy()
                else:
                    nnum = chlist[0]
                countdict[nnum] += 1
                start = nnum
                chlist = Card(chlist).copy()
            else:
                countdict[busu] += 1
                start = busu

#选择前n个最大的值，并且输出字符串
def Str(exdict, N, M):
    sdict = sorted(exdict.items(), key = lambda x: x[1], reverse = True)
    ncount = 0
    strkey = ''
    while ncount < N:
        item = sdict[ncount]

        if len(str(item[0])) < 2:
            strkey += '0%s'%item[0]
            print('0%s ：%.4f%%\n'%(item[0], exdict[item[0]] / M * 100))
        else:
            strkey += '%s' % item[0]
            print('%s ：%.4f%%' % (item[0], exdict[item[0]] / M * 100))
        ncount += 1
    return strkey

print('模拟完毕后，每个方格的停留次数：%s'%countdict)
print(Str(countdict, 3, monitimes))
#答案：
#模拟完毕后，每个方格的停留次数：{0: 276, 1: 185, 2: 148, 3: 201, 4: 217, 5: 275, 6: 208, 7: 80, 8: 198, 9: 218, 10: 762, 11: 212, 12: 250, 13: 246, 14: 302, 15: 380, 16: 309, 17: 287, 18: 293, 19: 289, 20: 308, 21: 301, 22: 113, 23: 280, 24: 356, 25: 304, 26: 256, 27: 258, 28: 281, 29: 296, 30: 0, 31: 293, 32: 225, 33: 225, 34: 248, 35: 181, 36: 75, 37: 197, 38: 216, 39: 251}
##3个停下概率最大的方格：
#10 ：7.6200%
#15 ：3.8000%
#24 ：3.5600%
##6位数字串：
#101524
