#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany

an_dict={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
         8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
         14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
         19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
         70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'onethousand'}#数字英文字典
fan=[]
for i in range(1,1001):
    if i<=20:
        fan.append(an_dict[i])#不大于20都是固定的
    elif i>20 and i<=100:
        if i==100:
            fan.append('onehundred')#表示100
        else:
            fan.append(str(an_dict[int(i/10)*10])+str(an_dict[i-int(i/10)*10]))
    else:
        if i==1000:
            fan.append(an_dict[1000])
        else:
            if i-int(i/100)*100<=20 and i-int(i/100)*100>0 :
                fan.append(str(an_dict[int(i/100)])+str(an_dict[100])+
                           str('and')+str(an_dict[i-int(i/100)*100]))
            elif i-int(i/100)*100==0:
                fan.append(str(an_dict[int(i/100)])+str(an_dict[100]))
            else:       fan.append(str(an_dict[int(i/100)])+str(an_dict[100])+str('and')+str(an_dict[i-int(i/100)*100-(i-int(i/10)*10)])+str(an_dict[i-int(i/10)*10]))
#开始计数
fanan=''
for i in fan:
    if i!='':
        fanan+=i
print(len(fanan))
