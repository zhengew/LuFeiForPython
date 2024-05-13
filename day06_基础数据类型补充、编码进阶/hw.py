# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: hw.py
# @datatime: 2024/3/22 09:55

# 字典 增删改
# 字典创建方式
# 1. dict()  参数为元组列表，元组第一个元素为key, 第二个元素为value
d1 = dict([('name', 'alex'), ('age', 18)])
print(d1, type(d1))

# 2. dict() 参数为 关键字参数
d2 = dict(name='alex', age=18)
print(d2, type(d2))

# 3. dict() 参数为 字典
d3 = dict({'name':'alex', 'age': 18})
print(d3, type(d3))

# 4. 直接创建字典
d4 = {'name': 'alex', 'age': 18}
print(d4, type(d4))

# 5. dict 参数 用 zip函数+元组拆包
d5 = dict(zip(('name', 'alex'), ('age', 18)))
print(d5, type(d5))

# 6. 字典推导式
d6 = {k: v for k, v in [('name', 'alex'), ('age', 18)]}
print(d6, type(d6))

# 7. fromkeys() 函数， 第一个参数为可迭代对象，可迭代对象的元素为不可变类型，作为字典的key, 第二个参数为字典的 value,
d7 = dict.fromkeys(['name', 'age'], None)
print(d7, type(d7))