# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 集合.py
# @datatime: 2024/5/21 19:45

# 集合
# 1. 特点： 无序、元素不可重复、集合本身是可变类型，集合的元素必须是不可变类型：str int bool tuple
# frozenset() 函数可以将集合强转成不可变类型
# s1 = set()
# s1 = frozenset(s1)

# 2. 应用场景
# 列表去重： 列表强转成集合去重，再强转成列表
# 求集合的 交集 并集 差集 反交集， 判断 子集和超集

# 创建
# 1. 创建空集合必须使用 set() 函数初始化， {} 创建的是字典类型
print(type(set()), type({})) # <class 'set'> <class 'dict'>

# 2. 初始化集合并赋值
s1 = {1, 2, 3}
s2 = {1, }
s3 = {1}

print(type(s1), type(s2), type(s3)) # <class 'set'> <class 'set'> <class 'set'>

# 新增
# 1. add() 如果集合添加的元素是可变数据类型，则抛出typeError异常
s1 = set()

s1.add(1)
s1.add((1, 2))
print(s1) # <class 'set'> <class 'set'> <class 'set'>
# s1.add([]) # TypeError: unhashable type: 'list'

# 2. update(可迭代对象)  集合中迭代着追加可迭代对象中的元素，如果可迭代对象中存在可变数据类型，则抛出 typeError异常
print(s1) # {1, (1, 2)}
s1.update([1, 2, 3, 4])
print(s1) # {1, 2, 3, (1, 2), 4}

# s1.update([1, []]) # TypeError: unhashable type: 'list'

# 删除
# 1. remove(value)  # 如果被删除元素不存在，则抛出keyError异常
s1 = {1, 2, 3, 4, 5}
s1.remove(1)
print(s1) # {2, 3, 4, 5}
# s1.remove(6) # KeyError: 6

# 2. pop() 随机删除集合中的一个元素,返回值为被删除的元素
print(s1)
res = s1.pop()
print(res)

# 3. clear()  清空集合
print(s1) # {3, 4, 5}
s1.clear()
print(s1) # set()

# 4. del 集合对象， 被删除后继续引用该变量会抛出 nameError异常
del s1
# print(s1)  # NameError: name 's1' is not defined. Did you mean: 's2'?


# 查询
# 集合不支持 索引查询和切片查询， 可以遍历查询、集合推导式过滤数据
s1 = set()
s1.update([i for i in range(11)])
print(s1)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 1. 循环遍历
for i in s1:
    print(i, end=' ')
print()

# 2. 集合推导式过滤数据
s2 = {i for i in s1 if i % 2 == 0}
print(s2) # {0, 2, 4, 6, 8, 10}

# 交并差集、 反交集、 子集和超集
s1 = {1, 2 ,3}
s2 = {1, 2, 3, 4, 5, 6}

# 1. 交集 &
print(s1 & s2) # {1, 2, 3}

# 2. 并集
print(s1 | s2) # {1, 2, 3, 4, 5, 6}

# 3. 差集
print(s2 - s1) # {4, 5, 6}

# 4. 反交集
print(s1 ^ s2) # {4, 5, 6}

# 5. 子集 ，返回值为 True / False
print(s1 < s2) # True

# 6. 超集， 返回值为 True / False
print(s2 > s1) # True


# 集合强转成 不可变类型
s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s1 = frozenset(s1)

print(type(s1)) # <class 'frozenset'>
