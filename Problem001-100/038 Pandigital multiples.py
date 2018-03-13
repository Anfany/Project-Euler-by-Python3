#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem038 Pandigital multiples

def an_fan(lisa):#判断数是否为全数字的数
    for i in lisa:
        if lisa.count(i)>1 or '0' in lisa:
            return False
    return True
anfan=0
for i in range(1,9999):
    fanan=str(i)#乘积从1开始
    j=2
    while True:
        fanan+=str(i*j)
        j+=1
        if len(fanan)>9:#只有长度正好为9才可能满足条件
            break
        elif len(fanan)<9:
            pass
        else:
            if an_fan(fanan):
                if anfan<int(fanan):#选择最大的
                    anfan=int(fanan)
print(anfan)
#答案：932718654
