#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


hu=list(range(1,22))
hh=[]
i=0
while i<21:
    hh.append(hu[:])
    i+=1
for j in range(0,21):
    hh[0][j]=1  
for ii in range(0,20):
    for ji in range(0,20):
        hh[ii+1][ji+1]=hh[ii][ji+1]+hh[ii+1][ji]
print(hh[20][20])
