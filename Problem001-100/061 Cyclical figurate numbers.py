#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
#Author: AnFany


# Problem061 Cyclical figurate numbers

# 三角数n*(1*n-(-1))/2、四方数n*(2*n-0)/2
# 五星数n*(3*n-1)/2、六点数n*(4*n-2)/2
# 七顶数n*(5*n-3)/2、八边数n*(6*n-4)/2
# 综合函数
def All(n, m):  # m代表三、四……八
    return n * ((m - 2) * n - (m - 4)) / 2
# 函数名称集合
FuncSet = ['Triangle', 'Square', 'Pentagon', 'Heptagon', 'Hexagon', 'Octagon']
# 四位数第三位不为0的数字分裂字典
def NumSet(func, m):
    fset = {}
    hu = 1
    while len(str(int(func(hu, m)))) < 5:
        cc = str(int(func(hu, m)))
        if len(cc) == 4 and cc[2] != '0':  # 四位数中的十位数不能为0
            if int(cc[:2]) not in fset:
                fset[int(cc[:2])] = [int(cc[2:])]
            else:
                fset[int(cc[:2])].append(int(cc[2:]))  # 前2位数字相同的
        hu += 1
    return fset
# 开始计算每个函数的字典集合
Set = locals()
for an in [5, 4, 3, 2, 0, 1]:
    Set['%s' % FuncSet[an]] = NumSet(All, an + 3)

# 无法判断这几个数字分别是什么型的函数
# 需要遍历所有组合
# 但是不必全排列，因为1234、2341、3412,4123都是一样的
from itertools import permutations
zuhe = []
for j in permutations(FuncSet[1:]):
    zuhe.append([FuncSet[0]] + list(j))  # 固定一个,后面的全排列
# 递推函数
def Re(result, funlist, zuhelist):
    if len(result) == 6:
        if result[0][0] == result[-1][-1]:
            print(funlist)
            return result
        else:
            return False
    else:  # 需要继续添加
        for hg in zuhelist:
            if result[-1][-1] in eval(hg):
                for hu in eval(hg)[result[-1][-1]]:
                    dd = result.copy()
                    dd.append([result[-1][-1], hu])
                    rr = funlist.copy()
                    rr.append(hg)
                    ss = zuhelist.copy()
                    ss.remove(hg)
                    ff = Re(dd, rr, ss)
                    if ff:
                        return ff
                    else:
                        continue
        return False
# 开始
for huus in zuhe:  # 遍历每一种可能性
    # 记录数据
    record = []
    # 记录函数
    func = []
    # 选取起始的数据
    for start in eval(huus[0]):
        record = eval(huus[0])[start]
        func = [huus[0]]
        for jj in record:
            result = Re([[start, jj]], func, huus[1:])
            if not result:
                continue
            else:
                # 已经得出结果计算值
                print(result)
                summ = 0
                for num in result:
                    summ += int(str(num[0]) + str(num[1]))
                break
    break
print(summ)
#答案：数分别是：[[82, 56], [56, 25], [25, 12], [12, 81], [81, 28], [28, 82]]
#数对应的类型：['Triangle', 'Square', 'Hexagon', 'Octagon', 'Heptagon', 'Pentagon']
#总和：28684
