# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: tuple.py
# @datatime: 2024/3/14 10:09

# tuple 元组： 不可变数据类型，只可以查看，不能增删改，常用于元组拆包
# 用途：将一些比较重要不希望改动的数据放在元组中，只供查看；常用于元组拆包
# 1. 元组创建
# 用小括号包起来的任意元组，括号内只有一个元素时，如果元素后没有加上逗号，数据类型还是元素本身，如果加上逗号，数据类型就是元组
# l1 = (1)
# print(l1, type(l1)) # 1 <class 'int'>
# l2 = ('alex')
# print(l2, type(l2)) # alex <class 'str'>
# l3 = (1,)
# print(l3, type(l3)) # (1,) <class 'tuple'>
#
# l4 = tuple() # 元组是不可变类型，创建一个空的元组时没有意义的
# print(l4, type(l4)) # () <class 'tuple'>

# 2. 元组的查询
# l5 = (1, 1, 2, 2, 3)
# # 索引查
# print(l5[0]) # 1
# # 切片查
# print(l5[::2]) # (1, 2, 3)
# # 循环遍历
# for index, value in enumerate(l5, 1):
#     print(f'元组l5中的第{index}个元组值：{value}')

# 元组的其他方法
# 1. index 查找元素再元组中的索引位置, 可切片查询，找不到就抛出ValueError异常:ValueError: tuple.index(x): x not in tuple
l1 = (1, 1, 2, 2, 3)
# print(l1.index(1))
# print(l1.index(1, 1, -1))
# print(l1.index(5)) # ValueError: tuple.index(x): x not in tuple

# 2. count 统计某个元素再元组中出现的次数，没有则返回0
# print(l1.count(1)) # 2
# print(l1.count(5)) # 0

# 3. len 获取元组长度
# print(len(l1)) # 5
# print(l1.__len__()) # 5

# 4. 元组拆包
# a, b = ('alex', 'wusir')
# print(a, b)

t1 = tuple('1')
print(t1, type(t1))

t2 = (1,)
print(t2, type(t2))

# t3 = tuple(1)

t4 = ()
print(t4, type(t4))

t5 = tuple(i for i in range(10))
print(t5, type(t5))

