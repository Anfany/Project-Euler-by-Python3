#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem011 Largest product in a grid

fan= open(r'C:\Users\lenovo\Desktop\matrix.txt')
an=[]
for i in range(20):#读取数据
    an.append([])
    x =fan.readline()
    for j in range(20):
        an[i].append(int(x[j*3:(j*3)+2]))
def an_product(aflist):#计算乘积
    anfan=1
    for i in aflist:
        anfan*=i
    return anfan
def an_select_number(aflist):#选择数字
    n=len(aflist)
    m=len(aflist[0])
    anan=[]
    for i in range(n):
        fanfan=[]
        for j in range(m):
            try:
                leri=an_product(aflist[i][j:j+3])#左右方向
            except IndexError:#这么写就不用考虑超出范围
                leri=-1
            try:
                updo=an_product([aflist[i][j],aflist[i+1][j],aflist[i+2][j],aflist[i+3][j]])#上下方向
            except IndexError:
                updo=-1
            try:
                rido=an_product([aflist[i][j],aflist[i+1][j+1],aflist[i+2][j+2],aflist[i+3][j+3]])#左上右下对角线方向
            except IndexError:
                rido=-1
            try:
                leup=an_product([aflist[i][j],aflist[i+1][j-1],aflist[i+2][j-2],aflist[i+3][j-3]])#左下右上对角线方向
            except IndexError:
                leup=-1
            nu=max(leri,updo,rido,leup)
            fanfan.append(nu)
        for jj in fanfan:
            anan.append(jj)
    return max(anan)           
print(an_select_number(an))
#答案：70600674
