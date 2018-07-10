#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem004 Largest palindrome product

def an_palindromic(number):  # 判断回文数
    num = str(number)
    if num == num[::-1]:
        return True

result = 0
for ip in range(100, 1000):
    for jp in range(100, 1000):
        pro = ip * jp
        if an_palindromic(pro):
            result = max([result, pro])

print(result)
#答案：993*913=906609
