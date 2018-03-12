#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


an_month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
def year_day(year):#判断一年的天数
    if year%400==0:
        day=366
    elif year%4==0 and year%100!=0:
        day=366
    else:
        day=365
    return day

def month_day(year,an_mo):#判断一年中一个月的天数字典
    day_dict={}
    for i in an_mo:
        if i=='Apr' or i=='Jun' or i=='Sep' or i=='Nov':
            day_dict[i]=30
        elif i=='Feb' and year_day(year)==366:
            day_dict[i]=29
        elif i=='Feb' and year_day(year)==365:
            day_dict[i]=28
        else:
            day_dict[i]=31
    return day_dict

anan_fan=[]#记录天数序列
for i in range(1901,2001):
    gh=month_day(i,an_month)
    for jjj in an_month:
        anan_fan.append(gh[jjj])
anan_fan.insert(0,year_day(1900))#天数序列加上1900年的天数
Sunday=0#记录1号是星期天
days=1#距离1900年1月1日的天数
for day in anan_fan:
    days+=day
    if days%7==0:#只要距离1900年1月1日的天数是7的倍数，这个月的第一天就是星期日
        Sunday+=1
print(Sunday)
