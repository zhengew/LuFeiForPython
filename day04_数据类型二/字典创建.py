# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 字段.py
# @datatime: 2024/3/14 15:58

# 字典
# 字典的key: 不可变类型，可哈希  int str tuple bool
# 字典的Value: 任意数据类型

# 哈希值 hash()
# info = hash('alex is dsb')
# print(info) # 4483632643058032962

# 1. 创建字典
# 方式一  dict()  实参类型为列表或元组，实参中的元素为元组，元组中第一元素为字典的key, 第二个元素为字典的value
d1 = dict([('name', 'alex'), ('age', 18)])
print(d1, type(d1)) # {'name': 'alex', 'age': 18} <class 'dict'>

# 方式二  dict()  实参以关键字参数形式传递
d1 = dict(name='alex', age=18)
print(d1, type(d1)) # {'name': 'alex', 'age': 18} <class 'dict'>

# 方式三 dict() 实参为字典类型数据
d1 = dict({'name': 'alex', 'age': 18})
print(d1, type(d1)) # {'name': 'alex', 'age': 18} <class 'dict'>

# 方式四 直接创建字典
d1 = {}
print(d1, type(d1)) # {} <class 'dict'>

# 方式五 dict() 实参通过 zip() 函数解包，zip 中的参数为两个长度相等的列表或元组，zip第一个参数中元素值为不可变数据类型,如果长度不想等，则以第一个参数为准组陈 key:value键值对
d1 = dict(zip((1, 2, 3), ('a', 'b', 'c', 'd')))
print(d1, type(d1))

# 方式六 字段推导式， 循环列表，再通过列表拆包给 key和value赋值
d1 = {x:y for x, y in [('name', 'alex'), ('age', 18)]}
print(d1, type(d1)) # {'name': 'alex', 'age': 18} <class 'dict'>

# 方式七 dict.fromkeys(__iterable, __value) 函数，遍历实参可迭代类型作为key, key对应的value都为实参传递的value
d1 = dict.fromkeys(['name', 'age'], '') #
print(d1, type(d1)) # {'name': '', 'age': ''} <class 'dict'>
