#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem034 Digit factorials

an_dict={'0':1,'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880}
hu=0
for i in range(10,8*362880):
    ji=list(str(i))
    jde=0
    for ff in ji:
        jde+=an_dict[ff]
    if jde==i:#数字阶乘的和等于数
        hu+=i
        print('满足条件的数有：%d'%i)
print(hu)
#答案：满足条件的数有：145
#满足条件的数有：40585
#和为：40730
