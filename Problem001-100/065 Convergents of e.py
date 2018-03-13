#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem065 Convergents of e

def Computer(n):#n表示第几位
    if n==1:
        return 2,1
    elif n==2:
        return 3,1
    else:
        #计算属于第几个值
        #除去前2个值
        dd=n-2
        #列出n位之前经历的数字，例如第5位就是[1,1,2,1,2].从后往前
        #例如第6位就是[4,1,1,2,1,2]
        shuzilist=[2,1]#开始的2位
        for ii in range(dd):
            if ii%3==0:
                shuzilist.append((int(ii/3)+1)*2)
            else:
                shuzilist.append(1)
        slist=shuzilist[::-1]
        #其中slist中的第一位是起始数据
        fenmu=slist[0]
        fenzi=1
        for shuzi in slist[1:]:
            fenzi=fenmu*shuzi+fenzi#计算加法
            fenmu,fenzi=fenzi,fenmu#计算倒数
        return fenmu,fenzi

for jj in range(1, 14):
    fenshu = Computer(jj)
    print('第%s个逼近值：%d / %d'%(jj, fenshu[0], fenshu[1]))

result=Computer(100)[0]
print('第100位的分子数字和为：%d'%sum([int(x) for x in list(str(result))]))
#答案：第1个逼近值：2 / 1
#第2个逼近值：3 / 1
#第3个逼近值：8 / 3
#第4个逼近值：11 / 4
#第5个逼近值：19 / 7
#第6个逼近值：87 / 32
#第7个逼近值：106 / 39
#第8个逼近值：193 / 71
#第9个逼近值：1264 / 465
#第10个逼近值：1457 / 536
#第11个逼近值：2721 / 1001
#第12个逼近值：23225 / 8544
#第13个逼近值：25946 / 9545
#第100位的分子数字和为：272
