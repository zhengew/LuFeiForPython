# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 字典.py
# @datatime: 2024/5/13 19:42

# 字典：可变数据类型，元素为 key:valaue形式， key 为不可变数据类型(可哈希， str, int, tuple, bool)，value为任意数据类型
# 哈希值 hash()
print(hash((1,))) # -6644214454873602895

# 字典创建方式
# 1. 直接创建
d1 = {}
d2 = {'name': 'alex', 'age': 18}
print(d1, type(d1), '\t', d2, type(d2))

# 2. dict(关键字参数)
d1 = dict(name='alex', age=18)
print(d1)

# 3. dict(直接传字典)
d1 = dict({'name': 'alex', 'age': 18})
print(d1)

# 4. dict(参数为元组列表，元组中的元素为字典的key和value)
d1 = dict([('name', 'alex'), ('age', 18)])
print(d1)

# 5. dict(zip(元组列表，列表的第一个元组为字典的key, 第二个元素为字典的value, 如果元组中的元素数量不同，以第一个元素为准))
d1 = dict(zip(('name', 'age'), ('alex', 18)))
print(d1)

d2 = dict(zip((1, 2, 3), ('a', 'b', 'c', 'd')))
print(d2)  # {1: 'a', 2: 'b', 3: 'c'}

# 6. dict.fromkeys 函数，第一个参数为字典的key, 第二个参数为所有key对应的默认值，默认为None
d1 = dict.fromkeys(('name', 'age', 'hobby'))
print(d1) # {'name': None, 'age': None, 'hobby': None}

d2 = dict.fromkeys(('name', 'age', 'hobby'), '')
print(d2) # {'name': '', 'age': '', 'hobby': ''}


# 字典的增删改查
d1 = dict(dict.fromkeys(('name', 'age')))
# 增
# 1. 通过字典的key直接赋值，如果key存在则改变原值，不存在则增加键值对
d1['name'] = 'alex'
print(d1, type(d1)) # {'name': 'alex', 'age': None}

# 2.setdefault 函数， 第一个参数为字典的key, 第二个参数为key对应的value, 默认为None, 如果key 存在则不改变原值，不存在则增加键值对,
# 有返回值，返回值为 key对应的value

value = d1.setdefault('name', 'taibai')
print(f'd1中存在键为nmae的元素，所以value的值不改变，仍为原值:{value}') # d1中存在键为nmae的元素，所以value的值不改变，仍为原值:alex

value = d1.setdefault('hoby', 'run')
print(value, d1) # run {'name': 'alex', 'age': None, 'hoby': 'run'}

# 3. 通过 fromkeys 函数设置字典默认值，第一个参数为可迭代类型，元素为字典的key, 第二个参数为 key的默认值
d1 = dict.fromkeys(('name', 'birghday', 'hobby'), None)
print(d1) # {'name': None, 'birghday': None, 'hobby': None}


# 删除
d1 = dict(zip((1, 2, 3, 4), ('a', 'b', 'c', 'd')))
print(d1) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 1. pop()  第一个参数为字典的key, 返回值为 key对应的value, 如果key不存在且没有指定默认值，则抛出keyError异常，指定默认值则返回默认值

# value = d1.pop(5)
# print(value) # KeyError: 5

value = d1.pop(5, 'Key不存在')
print(value) # Key不存在

value = d1.pop(4)
print(value) # d

# 2. popiteam py3.5之前为随机删除一个键值对，3.5及以后为删除最后一个键值对，返回值类型为数组形式，第一个元素为被删除的key,第一个元素为key对应的value
print(d1)
value =d1.popitem()
print(value) # (3, 'c')

# 3. del 字典[key]  通过key删除, key不存在则抛出 keyError异常
print(d1)
# del d1[6] # KeyError: 6

del d1[2]
print(d1) # {1: 'a'}

# 4. clear 清空字典
d1.clear()
print(d1) # {}

# 5. del 引用字典的变量
# del d1
# print(d1) # NameError: name 'd1' is not defined. Did you mean: 'd2'?

# py内存管理机制：引用技术、标记删除、分代回收

# 修改
d1 = {1: 'a', 2: 'b', 3: 'c'}
# 1. 通过 key 直接改, 如果key不存在则增加键值对
d1[3] = 'C'
print(d1)

# 2. update函数， 如果key不存在则增加键值对，存在则改变原值

# update 函数参数为关键字参数传参，key = value, key存在则改值，不存在则增加键值对
print(d1)
d1.update(name='alex', hoby='run')
print(d1)

# update 函数参数为 元组列表，元组中的元组为字典的 key和value, key存在则改值，不存在则增加键值对
d1.update([('sex', 'man'), ('hobby', '抽烟喝酒唐突')])
print(d1)

# update 函数参数为字典，如果实参中的key存在则改值，不存在则增加键值对
d1.update({'name': '太白', 'sex': 'female'})
print(d1)

# 查询
# 1. 通过key直接查，返回值为key对应的value, 如果key不存在则抛出keyError 异常
print(d1)
value = d1['name']
print(value)

# value = d1['age'] # KeyError: 'age'


# 2. get 函数， 第一个参数为字典的key, 第二个参数可指定key不存在时的返回值，默认返回None
value = d1.get('name')
print(value)

value = d1.get('birthday')
print(value) # None

value = d1.get('birthday', 'Key不不存在')
print(value) # Key不不存在

# 字典的其他方法
# 1. keys()  获取字典所有的key,返回值为 dict_keys类型数据
print(d1)
key_data = d1.keys()
print(key_data) # dict_keys([1, 2, 3, 'name', 'hoby', 'sex', 'hobby'])

# 2. values()  获取字典所有的value, 返回值为 dict_values 类型数据
value_data = d1.values()
print(value_data)  # dict_values(['a', 'b', 'C', '太白', 'run', 'female', '抽烟喝酒唐突'])

# 3. items() 获取字典所有的 key 和 value, 返回值类型为 dict_items, 元组列表， 元组中的元素为字典的 key 和 value, 一般和 enumerate 一起使用
key_value_data = d1.items()
print(key_value_data)

for num, data in enumerate(d1.items(), 1):
    key, value = data
    print(num, key, value)