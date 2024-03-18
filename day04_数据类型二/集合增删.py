# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 集合增删.py
# @datatime: 2024/3/18 10:11

# 集合的增删及交并差集，子集和超集

s1 = set()

# 增加
# 方式一 add(__element)
s1.add('alex')
print(s1) # {'alex'}

# 方式二 update(__iterable)  迭代着追加，如果需要批量追加到集合中，可以使用update, 前提是 实参中的元素为不可变类型
s1.update(['alex', 'wusir'])
print(s1) # {'alex', 'wusir'}

s1.update('abcdefg')
print(s1) # {'alex', 'wusir', 'c', 'b', 'a'}


# 删除
# 方式一：remove(__element)  删除集合中的某个元素
s1.remove('a')
print(s1) # {'alex', 'wusir', 'd', 'c', 'e', 'g', 'b', 'f'}

# 方式二： pop()  随机删除一个元素, 返回值为被删除的元素
a = s1.pop()
print(s1, f'被删除的元素为：{a}') # {'e', 'wusir', 'g', 'alex', 'f', 'b', 'c'} 被删除的元素为：d

# 方式三： clear() 清空集合
s1.clear()
print(s1, type(s1)) # set() <class 'set'>

# 方式四： del 引用集合的变量
del s1
# print(s1, type(s1)) # NameError: name 's1' is not defined


# 集合的其他操作 交并差 反交集(两个集合去掉交集部分的剩余元素) 、 子集、超集
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 交集
res = s1 & s2
print(res, type(res)) # {4, 5} <class 'set'>

# 并集
res = s1 | s2
print(res, type(res)) # {1, 2, 3, 4, 5, 6, 7, 8} <class 'set'>

# 差集
res = s1 - s2
print(res, type(res)) # {1, 2, 3} <class 'set'>

# 反交集
res = s1 ^ s2
print(res, type(res)) # {1, 2, 3, 6, 7, 8} <class 'set'>

# 子集和超集，返回值为bool值
# 子集
s3 = {1, 2, 3}
s4 = {1, 2, 3, 4, 5, 6}
res = s3 < s4
print(res, type(res)) # True <class 'bool'>

# 超集
res = s4 > s3
print(res, type(res)) # True <class 'bool'>


#  frozenset 将集合变成不可变类型
s1 = {1, 2, 3}
s1 = frozenset(s1)
print(s1, type(s1)) # frozenset({1, 2, 3}) <class 'frozenset'>

# s1.add(1) # AttributeError: 'frozenset' object has no attribute 'add'