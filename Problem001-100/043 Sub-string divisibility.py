#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem043 Sub-string divisibility

from itertools import permutations as ip#引入组合库
hh=[''.join(list(i)) for i in list(ip('1023456789'))]
alldigit = []
for i in hh:
    if i[0]!='0':
        if int(i[7:10])%17==0:
            if int(i[6:9])%13==0:
                if int(i[5:8])%11==0:
                    if int(i[4:7])%7==0:
                        if i[5] in ['0','5']:
                            if int(i[2:5])%3==0:
                                if int(i[3])%2==0:
                                    alldigit.append(int(i))
print(alldigit)
print(sum(alldigit))
#答案：满足此条件的数：[1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
#所有数之和：16695334890
