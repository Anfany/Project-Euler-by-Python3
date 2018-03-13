#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem032 Pandigital products

def anfan(n1,n2):#判断是否是全数字的
    a=list(str(n1))+list(str(n2))+list(str(n1*n2))
    hu=list(range(1,10))
    b=[]
    for i in hu:
        b.append(str(i))
    if b==sorted(a):     
        return True
def fanan(n1):#判断数是否含有重复数字
    if len(list(str(n1)))==len(set(list(str(n1)))):
        return True
ana=[]#存储乘积结果
fana = []#存储表达式
#因数分别在(100, 1000) 和（10，100）之间
for i in range(100,1000):
    if fanan(i):
        for j in range(10,100):
            if fanan(j):
                if anfan(i,j):
                    ana.append(i*j)
                    fana.append('%d*%d=%d'%(i,j,i*j))
                elif len(list(str(i*j)))>=5:#乘积只有小于5位数才可能为全数字的
                    break
#因数分别在(2, 10) 和（1000，5000）之间                
for i in range(2,10):
    if fanan(i):
        for j in range(1000,5000):
            if fanan(j):
                if anfan(i,j):
                    ana.append(i*j)
                    fana.append('%d*%d=%d'%(i,j,i*j))
                elif len(list(str(i*j)))>=5:#乘积只有小于5位数才可能为全数字的
                    break
print(fana)
print(sum(g for g in set(ana)))
#答案：['138*42=5796', '157*28=4396', '159*48=7632', '186*39=7254', '198*27=5346', '297*18=5346', '483*12=5796', '4*1738=6952', '4*1963=7852']
#全数字乘积式之和[重复的只计算一次]：45228
