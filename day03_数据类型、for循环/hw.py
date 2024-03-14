# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: hw.py
# @datatime: 2024/3/12 15:12


# l1 = ['abc', 'def', 'ghi', 'jkl', '111.xml', '0 Mar']
# l1 = list(filter(lambda y: '0 Mar' not in y, filter(lambda x: '.xml' not in x, l1)))
# print(l1)


# 列表创建
# # 1.
# l1 = [1, 2, 3]
# # 2.
# l2 = list()
# # 3
# l3 = [i for i in range(1, 11)]
# print(l1, l2, l3) # [1, 2, 3] [] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 列表增
# l1 = list()
# # 1. append  追加
# l1.append('1')
# # 2. 指定索引位置追加
# l1.insert(1, '2')
# # 3.
# l1.extend('abcdefg')
# print(l1)
#
# l1.append(3)
# print(l1)
# l1.insert(len(l1), '4')
# print(l1, len(l1))

# 列表改
# # 1. 索引改
# l1 = [i for i in range(11)]
# l1[-1] = 11
# print(l1)
#
# # 2.切片改 切片改列表时，可迭代对象的值必须与切片后替换的值一一对应
# l1[::2] = 'abcdef'
# print(l1)

# 列表删
# l1 = [i for i in range(10)]
# 1. pop() 默认删除列表最后一个元素，返回值为被删除的列表元素，可以指定索引位置删除
# n = l1.pop()
# print(n)

# 2. remove(value) 按value删, 如果删除的值不存在，则抛出ValueError异常 ValueError: list.remove(x): x not in list
# l1.remove(9)
# print(l1)
# l1.remove(10)

# 3. clear()  清空列表
# l1.clear()
# print(l1) # []

# 4. del 按索引删除, 如果索引越界，则抛出 IndexError 异常 IndexError: list assignment index out of range
# del l1[-1]
# print(l1)

# 5. 切片删除
# del l1[::2]
# print(l1)

# 列表其他操作
# 1. count 统计列表中某个元素出现的次数
l1 = [i for i in range(1, 11)] + [i for i in range(1, 6)]
# print(l1)
#
# n = l1.count(5)
# print(n) # 2
# print(l1.count(11))

# 2. index 找出列表中某个值第一次出现时的索引位置, 如果未匹配到，则抛出 ValueError异常 ValueError: 11 is not in list
# index_num = l1.index(5)
# print(index_num) # 4
# index_num2 = l1.index(11) # ValueError: 11 is not in list

# 3. 列表排序  sort()  正序， resverse() 倒序
# l1.sort()
# print(l1)  # [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
#
# l1.reverse()
# print(l1) # [10, 9, 8, 7, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]

# 4. 列表相加
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# print(l3)  # [1, 2, 3, 4, 5, 6]

# 5. 列表相乘
# l1 = [1, 2, 3] * 3
# print(l1)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]