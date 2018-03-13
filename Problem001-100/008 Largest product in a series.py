#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem008 Largest product in a series

#将以上数据复制到txt文件：secries.txt
an=[]#存储数据
for line in open(r'C:\Users\GWT9\Desktop\ss.txt'):#读取数据
    for i in line:
        for j in i:
            if j!='\n':
                an.append(int(j))
zuida=13        
fan={}#存储连续13个数字的乘积
for i in range(0,len(an)+1-zuida):
    ss=1
    for j in an[i:i+zuida]:
        ss*=j
    fan[i]=ss
#选择字典中值最大的对应的键值
maxkey=max(fan.items(),key=lambda x:x[1])
print(an[maxkey[0]:maxkey[0]+zuida])#[5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5]
print(maxkey)
#答案：23514624000
