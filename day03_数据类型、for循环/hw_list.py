# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: hw_list.py
# @datatime: 2024/3/12 16:39

l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
# print(len(l1)) # 5
# 列表中追加元素"seven",并输出添加后的列表
# l1.append('seven')
# print(l1) # ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou', 'seven']
# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# l1.insert(0, 'Tony')
# print(l1) # ['Tony', 'alex', 'WuSir', 'ritian', 'barry', 'wenzhou']
# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# l1[1] = 'Kelly'
# print(l1) # ['alex', 'Kelly', 'ritian', 'barry', 'wenzhou']
# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2=[1,"a",3,4,"heart"]
# l1 += l2
# print(l1) # ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou', 1, 'a', 3, 4, 'heart']
# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwert"
# l1 += s
# print(l1) # ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou', 'q', 'w', 'e', 'r', 't']
# 请删除列表中的元素"ritian",并输出添加后的列表
# l1.remove('ritian')
# print(l1) # ['alex', 'WuSir', 'barry', 'wenzhou']
# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# del_value = l1.pop(1)
# print(f'被删除的元素：{del_value}, 删除元素后的列表: {l1}') # 被删除的元素：WuSir, 删除元素后的列表: ['alex', 'ritian', 'barry', 'wenzhou']
# 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del l1[1:4]
# print(l1) # ['alex', 'wenzhou']


# s = 'ala l1'
# print(s.startswith('al'))
#
# print(s.rsplit('l', 1))
#
# print(s.strip('1'))
# print(s.replace('a', 'z'))
# # print(s.index('22'))
# print(s.capitalize())
# print(s.title())


data = [1,2,3,4,5,6,7,8,9]
# data.append(666)
# print(data)
# data.insert(1, 2)
# print(data)
#
# data.extend('abcdef')
# print(data)
# data.remove('zew')
print(data, type(data))
del data[1:2:2]
print(data)
data *= 0
    