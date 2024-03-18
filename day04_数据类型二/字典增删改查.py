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

# fromkeys(__iterable, __value)  第一个位置参数为可迭代类型，参数中的元素为字典的key, 第二个位置参数为字典key的初始值
# 如果第一个位置参数中的元素重复，字典会自动对key去重
d2 = dict.fromkeys(['name', 'sex', 'hobby', 'age', 'hobby'], None)
print(d2, type(d2)) # {'name': None, 'sex': None, 'hobby': None, 'age': None} <class 'dict'>


# 2. 删除
# pop(__key, __returnValue)   通过 key 删除，返回值为被删除key对应的value; 如果key不存在，可指定返回值
data = d1.pop('hobby', None)
print(data, d1) # run {'name': 'age', 'alex': 18, 'sex': 'female'}
data = d1.pop('hobby', None)
print(data, d1) # None {'name': 'age', 'alex': 18, 'sex': 'female'}

# popitem()  python3.5 前，随机删除，3.5及以后，删除最后一个键值对，返回值为被删除的键值对，类型为元组
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
# del d1
# print(d1, type(d1))

# python 内存管理方式：
'''
1. 引用计数
2. 标记清除
3. 分代回收
'''

# 2. 修改
d1 = {'name': 'alex', 'age': 18}

# 键值对直接修改
d1['age'] = 30
print(d1) # {'name': 'alex', 'age': 30}

# update(**kwargs)
# 方式一： 实参为关键字参数，如果key存在则改值，不存在则增加键值对
d1.update(sex='male', age=40)
print(d1)
# 方式二：实参为元组列表，遍历列表并元组拆包，如果key存在则修改值，不存在则增加键值对。
d1.update([('sex', 'female'), ('hobby', 'run')])
print(d1) # {'name': 'alex', 'age': 40, 'sex': 'female', 'hobby': 'run'}

# 方式三：实参为 字典类型，如果key在原字典中存在，则修改值，不存在则增加键值对
d1.update({'sex':'male', 'height': '182'})
print(d1) # {'name': 'alex', 'age': 40, 'sex': 'male', 'hobby': 'run', 'height': '182'}

# 3. 查询
# 方式一： 通过key查询，如果key不存在则抛出KeyError异常
data = d1['name']
print(data) # alex
# data = d1['weight'] # KeyError: 'weight'

# 方式二： get(__key, __message)  如果key存在，则返回value,不存在则返回None, 可指定key不存在时的返回值
data = d1.get('name', None)
print(data) # alex
data = d1.get('weight')
print(data) # None
data = d1.get('weight', 'KeyError: key not found')
print(data) # KeyError: key not found

# 方式三： keys()  返回字典所有的key, 返回值类型为 dict_keys, 类似于列表
key_list = d1.keys()
print(key_list, type(key_list)) # dict_keys(['name', 'age', 'sex', 'hobby', 'height']) <class 'dict_keys'>

# 方式四： values() 返回字典所有的value, 返回值类型为 dict_values, 类似于列表
value_list = d1.values()
print(value_list) # dict_values(['alex', 40, 'male', 'run', '182'])

# 方式五：items() 以元组列表形式返回字典所有的key和value, 返回值类型为 dict_itemms
key_value_list = d1.items()
print(key_value_list, type(key_value_list)) # dict_items([('name', 'alex'), ('age', 40), ('sex', 'male'), ('hobby', 'run'), ('height', '182')]) <class 'dict_items'>

for index, data in enumerate(d1.items(), 1):
    print(index, data[0], data[1])

l1 = enumerate(['a', 'b', 'c'], 1)
print(l1, list(l1))



