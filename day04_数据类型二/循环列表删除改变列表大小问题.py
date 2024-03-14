# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 循环列表删除改变列表大小问题.py
# @datatime: 2024/3/14 10:50

'''
有列表l1, l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除（不能一个一个删除，此l1只是举个例子，里面的元素不定）。
'''

# 方式一
# l1 = [11, 22, 33, 44, 55]
# l2 = list()
# for i in range(len(l1)):
#     if i%2 == 0:
#         l2.append(l1[i])
# l1 = l2
#
# print(l1)

# 方式二  列表切片步长, 再赋值
# l1 = l1[::2]
# print(l1)