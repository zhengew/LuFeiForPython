# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 集合.py
# @datatime: 2024/3/18 10:00

# 集合是无序的，不重复的数据集合，集合中元素是不可变类型(可哈希 int str bool tuple), 集合本身是可变类型，所以集合不能当字典的key
# 应用：
# 1.集合给列表去重
# 2. 取数据集的 交并差集

# 创建
# 注意创建空集合，必须用 set初始化集合，{} 创建的是字典类型
# 方式一
s1 = set()
print(s1, type(s1)) # set() <class 'set'>

# 方式二
s1 = {1, 2, 3, 'zew'}
print(s1, type(s1))

# 注意
# 1.
# {} 一对空大括号创建的是字典类型数据
# s1 = {}
# print(s1, type(s1)) # {} <class 'dict'>

# 2. 集合中的元素必须是不可变类型，可哈希的，否则会抛出 TypeError异常：TypeError: unhashable type: 'list'
# s1 = {1, 2, 3, []}
# print(s1, type(s1)) # TypeError: unhashable type: 'list'