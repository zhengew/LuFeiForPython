# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 字典增删改查.py
# @datatime: 2024/3/14 16:38

# 字典增删改查
d1 = dict(zip(('name', 'age'), ('alex', 18)))
print(d1, type(d1)) # {'name': 'age', 'alex': 18} <class 'dict'>

# 1. 增加
# 通过 字典key做赋值操作，如果key在字典中不存在，则增加，存在则改变key对应的value
d1['sex'] = 'male'
print(d1) # {'name': 'age', 'alex': 18, 'sex': 'male'}
d1['sex'] = 'female'
print(d1) # {'name': 'age', 'alex': 18, 'sex': 'female'}

# setdefault(__key, __default)  如果key不存在，则增加键值对，key存在，则不改变原值, 函数返回值为 key 对应的value
data = d1.setdefault('sex', 'male')
print(data, d1) # female {'name': 'age', 'alex': 18, 'sex': 'female'}
data = d1.setdefault('hobby', 'run')
print(data, d1) # run {'name': 'age', 'alex': 18, 'sex': 'female', 'hoby': 'run'}

# 2. 删除
# pop(__key, __returnValue)   通过 key 删除，返回值为被删除key对应的value; 如果key不存在，可指定返回值
data = d1.pop('hobby', None)
print(data, d1) # run {'name': 'age', 'alex': 18, 'sex': 'female'}
data = d1.pop('hobby', None)
print(data, d1) # None {'name': 'age', 'alex': 18, 'sex': 'female'}

# popitem()  python3.5 前，随机删除，3.5及以后，删除最后一个键值对，返回值为被删除的键值对，类型为元素
# print(d1)
data = d1.popitem()
print(data, type(data), d1) # ('sex', 'female') <class 'tuple'> {'name': 'age', 'alex': 18}

# del 删除键值对, 如果key不存在，则抛出KeyError异常：KeyError: 'age'
del d1['age']
print(d1)
# del d1['age']

# clear()  清空字典
d1.clear()
print(d1, type(d1)) # {} <class 'dict'>

# 删除字典 del 字典指向的变量 ， 引用字典的变量被删除后，再引用变量名会抛出 NameError异常：NameError: name 'd1' is not defined
del d1
# print(d1, type(d1))


# 2. 修改