# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 元组.py
# @datatime: 2024/5/13 19:22

# 元组： 不可变数据类型，常用于元组拆包，或者保存不可变的数据
# 创建
t1 = (1, 2)
t = () # 元组是不可变类型，所以创建一个空元组是没有意义的
t1 = (1)
print(f't1的数据类型是：{type(t1)}') # int  元组内如果只有一个元素，需要加上 逗号分割，否则创建的数据类型不是元组，而是元素本身的数据类型
t2 = (1,)
print(f't2的数据类型是：{type(t2)}') # tuple

# 查询
t1 = ('a', 'b', 'c', 'd', 'e')
# 1. 索引查
value = t1[0]
print(f'{t1}的第一个元素是：{value}')

# 2. 切片查,返回值类型是元组类型
values = t1[::2]
print(f'{t1}切片查，步长2的结果集：{values}, 数据类型是：{type(values)}')
values = t1[-1:]
print(type(values),values)

# 元组的其他方法
t1 = (1, 1, 2 ,3 ,4, 5)
# 1. index  查找元组中某个元素的索引值，如果元素不存在，则抛出 valueError异常
n = t1.index(3)
print(n)

# n= t1.index(6) # ValueError: tuple.index(x): x not in tuple
# print(n)

# count 统计元组中某个元素出现的次数，如果不存在则返回0
n = t1.count(1)
print(n) # 2

n = t1.count(6)
print(n) # 0

# len  元组长度
n = t1.__len__()
print(n) # 6
n = len(t1)
print(n) # 6

# 元组拆包, 注意用来接收元组元素的对象数量要和元组的元素数量相同
t1 = ('alex', 18)
name, age = t1
print(f'姓名:{name}, 年龄:{age}')