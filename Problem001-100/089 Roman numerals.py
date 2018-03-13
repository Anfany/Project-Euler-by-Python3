#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem089 Roman numerals

import re
romandict = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000,}
fan=open(r'C:\Users\GWT9\Desktop\p089_roman.txt')#数据文件
an =[]
while 1:
    x=fan.readline()
    if len(x) == 0:
        break
    an.append(x.replace('\n',''))
fan.close()

##正则表达式
reformat= ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
#Roman -->Arabic numerals
def RoToAr(exlist, exdict = romandict, exre = reformat):
    digit = []
    for jj in exlist:
        #满足减法法则
        subb = 0
        for rere in exre:
            result = re.findall(r'%s'%rere, jj)
            if len(result) != 0:
                for cc in result:
                    subb += 2 * exdict[cc[0]]
        summ = 0
        #总和
        for rr in jj:
            summ += exdict[rr]
        #存储
        digit.append(summ - subb)
    return digit

romandict = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
dictroman = {romandict[i] : i for i in romandict}

#Arabic numerals -->Roman
def ArtoRo(exlist, exdict = dictroman):
    #Arabic
    #arlist = RoToAr(exlist)
    #Roman number
    romanlist = sorted(list(exdict.keys()), reverse=True)
    #存储
    ar = []
    for aa in exlist:
        roman = ''
        while aa != 0:
            for jnum in romanlist:
                if aa >= jnum:
                    cc = int(aa / jnum)
                    roman += cc * exdict[jnum]
                    aa -= cc * jnum
        ar.append(roman)
    return ar
#Computer
arabic = RoToAr(an)
roman = ArtoRo(arabic)
sim = 0
for ii in range(len(an)):
    sim += len(an[ii]) - len(roman[ii])
print(sim)
#答案：743
