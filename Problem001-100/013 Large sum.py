#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem013 Large sum

an=[]
for line in open(r'C:\Users\lenovo\Desktop\number.txt'):
    an.append(line.strip('\n'))
fan=[]
for j in range(len(an[0])):
    sm=0
    afan=[]
    for i in range(len(an)):
        sm+=int(an[i][j])
    afan.append(sm)
    for g in afan:
        fan.append(g)
aaa=[0]
anfan=[]
for i in range(1,50):
    jin_number=int((fan[-i]+aaa[i-1])/10)
    aaa.append(jin_number)
    he_number=int((fan[-i]+aaa[i-1])/10)+fan[-i-1]
    anfan.append(he_number)
fanan=anfan[::-1]
fanan.append(fan[-1])
first_ten=[]
for i in range(len(fanan)):
    if i==0:
        first_ten.append(fanan[i])
    else:
        a=fanan[i]-int(fanan[i]/10)*10
        first_ten.append(a)
first=[]
dt=''
for i in first_ten:
    dt+=str(i)  
print(dt[0:10])
#答案：5537376230
