#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem079 Passcode derivation

import re
fan=open(r'C:\Users\GWT9\Desktop\keylog.txt')#数据文件
#利用正则表达式
an =[]#存储数据文件
digit = []
while 1:
    x=fan.readline()
    if len(x) == 0:
        break
    for ii  in x:
        if ii not in digit and ii !='\n':
            digit.append(ii)
    an.append(x)
fan.close()

pattern = []#存储所有正则的格式
for jj in an:
    red = r'^(.*%s.*%s.*%s.*)$'%(jj[0], jj[1], jj[2])
    if red not in pattern:
        pattern.append(red)
#计算开始最小的数，digit存储了这个密码用到的数字，根据此可计算开始匹配的最小的数
num = ''
for istr in sorted(digit):
    num += istr
if num[0] == '0':
    minnumer = int(num[1] + num[0] + num[2:])
else:
    minnumer = int(num)

#开始
sign = 1
while 1:
    strnumer = str(minnumer)
    for p in pattern:
        if not re.compile(p).match(strnumer):#只要匹配不上。匹配的数字就加1
            sign = 0
            break
    if sign == 1:#证明全部匹配上了。
        break
    minnumer = int(minnumer) + 1
    sign = 1
print(minnumer)
#答案：73162890
