# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: hw.py
# @datatime: 2024/3/15 15:01

# 1. 请将列表中的每个元素通过 "_" 链接起来。
l1 = ['apple', 'banana', 'cherry']
# print('_'.join(l1)) # apple_banana_cherry

# 循环遍历方式
# l2 = ''
# for i in l1:
#     l2 = l2 + i + '_'
# l2 = l2[:-1]
# print(l2)

# 2.请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
# v1 = (11, 22 ,33)
# v2 = [44, 55, 66]
# v2.extend(v1)
# print(v2) # [44, 55, 66, 11, 22, 33]