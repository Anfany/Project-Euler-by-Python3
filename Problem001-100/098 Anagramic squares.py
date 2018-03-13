#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem098 Anagramic squares

fan=open(r'C:\Users\GWT9\Desktop\p098_words.txt')#数据文件
#存储words的list
cclist =[]
fu = []
for i in fan:
    for j in i:
        if j != ',':
            if j != '"':
                fu.append(j)
        else:
            if len(fu) == 1:
                cclist.append(fu[0])
            else:
                cclist.append(('').join(fu))
            fu =[]
cclist.append(('').join(fu))

#获得重排字母对
pair = []
leng = len(cclist)
for iw in range(leng - 1):
    for jw in range(iw, leng):
        iwc, jwc= cclist[iw], cclist[jw]
        if len(iwc) == len(jwc) and sorted(iwc) == sorted(jwc) and iwc != jwc:
            pair.append([iwc, jwc])

#根据字母长度获得该长度范围内的完全平方数
def Squre(length):
    if length == 1:
        return [1, 4, 9]
    gu = [ji ** 2 for ji in range(int((10 ** (length - 1)) ** 0.5), int((10 ** length) ** 0.5))]
    return gu

#根据字母和数字的对应关系获得数字
def Getdigit(exdict, word):
    num = ''
    for hh in word:
        num += exdict[hh]
    return int(num)

print('WORDS PAIR：', pair)
#判断数字和word是否对应
def Judge(number, word):
    accdict = {}
    leng = len(word)
    for jj in range(leng):
        if jj not in accdict:
            accdict[word[jj]] = str(number)[jj]
    #根据字典反写数字与原来数字是否一样
    if Getdigit(accdict, word) == number:
        return accdict
    else:
        return  False

#根据word和数字，求pair word的对应数字
def Getnum(words1, digitset, words):
    fu = []
    for digit in digitset:
        if len(words1) == len(str(digit)) and len(set(words1)) == len(set(str(digit))):#初步判断数字和word是否匹配。
            cdict = Judge(digit, words1)#判断是否匹配
            if cdict:#如果匹配，输出字母和数字的对应字典
                gunum = Getdigit(cdict, words)
                if gunum in digitset:#如果这个数也是完全平方数
                    fu.append([digit, gunum])#输出结果
                    print('%s ==> %s' %([words1, words], fu[0]))
                    return fu
    return False

result = []
for kk in pair:
    setdi = Squre(len(kk[0]))
    number = Getnum(kk[0], setdi, kk[1])
    if number:
        result.append(max(number[0]))
print('最大的平方数：', max(result))
##答案：
#WORDS PAIR： [['ACT', 'CAT'], ['ARISE', 'RAISE'], ['BOARD', 'BROAD'], ['CARE', 'RACE'], ['CENTRE', 'RECENT'], ['COURSE', 'SOURCE'], ['CREATION', 'REACTION'], ['CREDIT', 'DIRECT'], ['DANGER', 'GARDEN'], ['DEAL', 'LEAD'], ['DOG', 'GOD'], ['EARN', 'NEAR'], ['EARTH', 'HEART'], ['EAST', 'SEAT'], ['EAT', 'TEA'], ['EXCEPT', 'EXPECT'], ['FILE', 'LIFE'], ['FORM', 'FROM'], ['FORMER', 'REFORM'], ['HATE', 'HEAT'], ['HOW', 'WHO'], ['IGNORE', 'REGION'], ['INTRODUCE', 'REDUCTION'], ['ITEM', 'TIME'], ['ITS', 'SIT'], ['LEAST', 'STEAL'], ['MALE', 'MEAL'], ['MEAN', 'NAME'], ['NIGHT', 'THING'], ['NO', 'ON'], ['NOTE', 'TONE'], ['NOW', 'OWN'], ['PHASE', 'SHAPE'], ['POST', 'SPOT'], ['POST', 'STOP'], ['QUIET', 'QUITE'], ['RATE', 'TEAR'], ['SHEET', 'THESE'], ['SHOUT', 'SOUTH'], ['SHUT', 'THUS'], ['SIGN', 'SING'], ['SPOT', 'STOP'], ['SURE', 'USER'], ['THROW', 'WORTH']]
#['BOARD', 'BROAD'] ==> [17689, 18769]
#['CARE', 'RACE'] ==> [1296, 9216]
#['DEAL', 'LEAD'] ==> [1764, 4761]
#['EAST', 'SEAT'] ==> [2916, 1296]
#['EAT', 'TEA'] ==> [256, 625]
#['FILE', 'LIFE'] ==> [1296, 9216]
#['HATE', 'HEAT'] ==> [1369, 1936]
#['HOW', 'WHO'] ==> [256, 625]
#['ITS', 'SIT'] ==> [256, 625]
#['MALE', 'MEAL'] ==> [1369, 1936]
#['MEAN', 'NAME'] ==> [2401, 1024]
#['NOTE', 'TONE'] ==> [1296, 9216]
#['NOW', 'OWN'] ==> [625, 256]
#['POST', 'SPOT'] ==> [2916, 1296]
#['POST', 'STOP'] ==> [1024, 2401]
#['RATE', 'TEAR'] ==> [1024, 2401]
#['SHUT', 'THUS'] ==> [1764, 4761]
#最大的平方数： 18769
