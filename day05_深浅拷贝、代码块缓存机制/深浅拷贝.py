# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 深浅拷贝.py
# @datatime: 2024/3/18 22:44

# 深浅拷贝

# 1. 浅拷贝 copy(__obj)
# - 会在内存中新开辟一个空间，存放这个copy的列表，但是列表中的元素还是沿用之前对象的内存地址，
# - 所以浅拷贝的对象内存地址不同，但是浅拷贝对象里的元素内存地址相同

l1 = [1, 2, 'alex', [3, 4]]
l2 = l1.copy() # 浅拷贝

print(l1 is l2, f'l2浅拷贝l1, l1的内存地址是:{id(l1)}, l2的内存地址是:{id(l2)}')
# False l2浅拷贝l1, l1的内存地址是:4448247744, l2的内存地址是:4448249600

print(l1[3] is l2[3], f'l2浅拷贝l1, l1的第3个元素内存地址:{id(l1[3])}, l2的第3个元素内存地址:{id(l2[3])}')
# True l2浅拷贝l1, l1的第3个元素内存地址:4377667584, l2的第3个元素内存地址:4377667584

# 2. 深拷贝 copy.deepcopy(__obj)
# - 会在内存中新开辟一个空间，存放这个deepcopy的列表
# - 原列表中不可变的数据类型还是沿用之前对象的内存地址
# - 原列表中可变的数据类型，会在内存中重新创建一份

import copy
l1 = [1, 2, 'alex', [3, 4]]
l2 = copy.deepcopy(l1)

print(l1 is l2, f'l2深拷贝l1, l1的内存地址是:{id(l1)}, l2的内存地址是:{id(l2)}')
# False l2深拷贝l1, l1的内存地址是:4502937600, l2的内存地址是:4502937856

print(l1[3] is l2[3], f'l2深拷贝l1, l1的第3个元素内存地址:{id(l1[3])}, l2的第3个元素内存地址:{id(l2[3])}')
# False l2深拷贝l1, l1的第3个元素内存地址:4333882752, l2的第3个元素内存地址:4335692224

print(id(l1[-1][0]), id(l2[-1][0])) # 4410310960 4410310960
l1[-1][0] = 'alex'
print(l1) # [1, 2, 'alex', ['alex', 4]]
print(l2) # [1, 2, 'alex', [3, 4]] # 深拷贝会在内存中重新创建原列表中可变的数据类型,重新开辟一块内存空间
