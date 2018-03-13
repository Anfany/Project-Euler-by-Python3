#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem059 XOR decryption

#读取文件
with open(r'C:\Users\GWT9\Desktop\p058_cipher.txt') as f:
    data = f.read()
f.closed
#因为密钥只由三个小写字母构成
zimu1 = []#使用第一个字母加密的
zimu2 = []#使用第二个字母加密的
zimu3 = []#使用第三个字母加密的

listzi = data.split(',')
for hu in range(len(listzi)):
    if hu % 3 == 0:
        zimu1.append(int(listzi[hu]))
    elif hu % 3 == 1:
        zimu2.append(int(listzi[hu]))
    else:
        zimu3.append(int(listzi[hu]))

# 十进制转二进制
def DeToBs(number):
    if number == 0:
        return '0'
    else:
        hu = ''
        while number != 0:
            if number % 2 == 0:
                hu += '0'
            else:
                hu += '1'
            number = int(number / 2)
    uh = hu[::-1]
    return uh

# 二进制转十进制
def BsToDe(binary):
    nu = 0
    for i in range(len(binary)):
        nu += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return nu

# 异或运算
def Trans(bs1, bs2):
    bbs1 = DeToBs(bs1)
    bbs2 = DeToBs(bs2)
    if bs1 >= bs2:
        while len(bbs2) < len(bbs1):
            rebbs2 = bbs2[::-1]
            rebbs2 += '0'
            bbs2 = rebbs2[::-1]
    else:
        while len(bbs1) < len(bbs2):
            rebbs1 = bbs1[::-1]
            rebbs1 += '0'
            bbs1 = rebbs1[::-1]
    # 进行异或
    xor = ''
    for dd in range(len(bbs1)):
        if bbs1[dd] == bbs2[dd]:
            xor += '0'
        else:
            xor += '1'
    return BsToDe(xor)

#解密后的ASCII码除了是[大小写字母，英文逗号,空格,句点]之外的越少，说明是密钥的可能性越大。
def JudeMiyue(milist, st):
    dd = []
    for im in milist:
        if Trans(im, st) >= 65 and Trans(im, st) <= 122:#
            pass
        else:
            #加上这个判断是必须的， 因为如果不加，无法判断真正的密钥是什么。
            if Trans(im, st) not in [32, 44, 46]:
                # 除去英文逗号,空格,句点。
                dd.append(Trans(im, st))
    return len(set(dd))

def Last(milist):
    du = {}
    st = 97#代表a的ASCII码
    while st <= 122:#代表z的ASCII码，遍历循环，找到最小的对应的字母
        gu = JudeMiyue(milist, st)
        du[st] = gu
        st += 1
    mink = min(du.items(), key=lambda x: x[1])[0]#判断最小的
    return mink

sumd = 0#存储ASCII码的和
yuanwen = ''#加密前的明文

names = locals()
for i in [1, 2, 3]:#三个加密文件
    names['fr%d'%i] = Last(eval('zimu%d' % i))
    print('第%d个字母密钥为：%s'%(i, chr(eval('fr%d'%i))))

for iz, jz, hz in zip(zimu1, zimu2, zimu3):
    number1 = Trans(fr1, iz)
    number2 = Trans(fr2, jz)
    number3 = Trans(fr3, hz)
    sumd += number3 + number1 + number2
    yuanwen += chr(number1) + chr(number2) + chr(number3)

print('原文为:%s'%(yuanwen + chr(Trans(fr1, zimu1[-1]))))#因为字母1多一个
print('所有的ASCII码的和为:%d'%(sumd + Trans(fr1, zimu1[-1])))
#答案：第1个字母密钥为：g
#第2个字母密钥为：o
#第3个字母密钥为：d
#原文为:(The Gospel of John, chapter 1) 
#1 In the beginning the Word already existed. He was with God, and he was God. 
#2 He was in the beginning with God. 
#3 He created everything there is. Nothing exists that he didn't make. 
#4 Life itself was in him, and this life gives light to everyone. 
#5 The light shines through the darkness, and the darkness can never extinguish it. 
#6 God sent John the Baptist 
#7 to tell everyone about the light so that everyone might believe because of his testimony. 
#8 John himself was not the light; he was only a witness to the light. 
#9 The one who is the true light, who gives light to everyone, was going to come into the world. 
#10 But although the world was made through him, the world didn't recognize him when he came. 
#11 Even in his own land and among his own people, he was not accepted. 
#12 But to all who believed him and accepted him, he gave the right to become children of God. 
#13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.
#14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father.
#所有的ASCII码的和为:107359
