#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem054 Poker hands

#将牌面转化为数字，比较大小
# 读取数据
with open(r'C:\Users\GWT9\Desktop\p054_poker.txt') as f:#读取数据
    data = f.read()
f.closed
playone = []#玩家1
playtwo = []#玩家2
start = 0
end = 29
while len(data[start:end]) != 0:
    so = data[start:end].split(' ')
    playone.append(so[:5])
    playtwo.append(so[5:])
    start += 30
    end += 30
# 级别字典,便于比较大小
level = {'HC': 1e0, 'OP': 1e2, 'TP': 1e4, 'TK': 1e6, \
         'S': 1e8, 'F': 1e10, 'FH': 1e12, 'FK': 1e14, \
         'SF': 1e16, 'RF': 1e18}#保证牌面的级别
# 数字表示
Number = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
# 牌面转换形式
def OutDict(exlist, cd=Number):
    fcod = []
    nuod = []
    for i in exlist:
        if i[0] in cd:
            nuod.append(cd[i[0]])
        else:
            nuod.append(int(i[0]))
        fcod.append(i[1])
    return fcod, nuod
# 判断顺子
def JudgeC(exlist):
    shu = list(sorted(exlist))
    q = 1
    sug = []
    for ij in range(len(shu)):
        sug.append(shu[ij] - q)
        q += 1
    if len(set(sug)) == 1:
        return True
    else:
        return False
def Judge(nplist, le=level, cd=Number):#计算牌面的值
    # 字典形式
    exd = OutDict(nplist)
    fc = exd[0]
    nu = exd[1]
    # 判断
    if len(set(fc)) == 1:#五张牌的花色一样
        if set(nu) == set(cd.values()):
            return le['RF']#同花大顺
        elif JudgeC(nu):
            return max(nu) * le['F']#同花
        else:
            return max(nu) * le['SF']#同花顺
    else:
        #
        if len(set(nu)) == 2:#四条，或者葫芦
            gu = list(set(nu))
            if gu.count(gu[0]) == 1:#四条
                return gu[1] * le['FK'] + gu[0] * le['HC']
            elif gu.count(gu[0]) == 2:#葫芦
                return gu[1] * le['FH'] + gu[0] * le['OP']
            elif gu.count(gu[0]) == 4:#四条
                return gu[1] * le['HC'] + gu[0] * le['FK']
            elif gu.count(gu[0]) == 3:#葫芦
                return gu[1] * le['OP'] + gu[0] * le['FH']
        elif len(set(nu)) == 3:#三条或者两对
            gu = list(set(nu))
            maxj = {}
            for i in gu:
                maxj[i] = nu.count(i)
            maxt = max(maxj.items(), key=lambda x: x[1])[1]
            rnum = 0
            if maxt == 3:#三条
                fu = []
                for ii in maxj:
                    if maxj[ii] == 3:
                        rnum += ii * le['TK']
                    else:
                        fu.append(ii)
                rnum += max(fu) * le['HC'] + min(fu) * le['HC'] * 0.01
                return rnum
            else:#两对
                fu = []
                for ia in maxj:
                    if maxj[ia] == 2:
                        fu.append(ia)
                    else:
                        rnum += ia * 0.01
                rnum += max(fu) * le['TP'] + min(fu) * le['OP']
                return rnum
        elif len(set(nu)) == 4:#对子
            rnum = 0
            fu = []
            for ii in nu:
                if nu.count(ii) == 2:
                    rnum += ii * le['OP']
                else:
                    fu.append(ii)
            fus = sorted(fu, reverse=True)
            time = 100
            er = 0
            for jj in fus:
                rnum += jj * le['HC'] / (time ** er)
                er += 1
            return rnum
        else:#单牌
            if JudgeC(nu):
                return max(nu) * le['S']
            fu = sorted(nu, reverse=True)
            rnum = 0
            time = 100
            er = 0
            for jj in fu:
                rnum += jj * le['HC'] / (time ** er)
                er += 1
            return rnum
winone = 0
for ipok in range(len(playone)):
    if Judge(playone[ipok]) > Judge(playtwo[ipok]):
        winone += 1
print(winone)
#答案：376
