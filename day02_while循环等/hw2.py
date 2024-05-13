# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: hw2.py
# @datatime: 2024/5/10 16:47

# 1.写代码，有如下列表，按照要求实现每一个功能

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
length = len(li)
print(f'列表{li}的长度是：{length}')


# 列表中追加元素"seven",并输出添加后的列表
li.append('seven')
print(li)

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li.insert(1, 'Tony')
print(li)

# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[1] = 'Kelly'
print(li)

# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
l2=[1,"a",3,4,"heart"]
# li += l2
# print(li)

li.extend(l2)
print(li)

# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = 'qwert'
li.extend(s)
print(li)

# 请删除列表中的元素"ritian",并输出添加后的列表
if 'ritian' in li:
    li.remove('ritian')
print(li)

# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
value = li.pop(1)
print(f'被删除的元素:{value}, 删除后的列表:{li}')


# 请删除列表中的第2至4个元素，并输出删除元素后的列表
# for i in range(len(li)):
#     if i >0 and i < 4:
#         li.pop(i)
# print(li)

del li[1:4]
print(li)


# 2. 2.写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
l1 = li[:3]
print(l1)
# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
l2 = li[3:6]
print(l2)

# 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
l3 = li[::2]
print(l3)


# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
l4 = li[1:-2:2]
print(l4)
# 通过对li列表的切片形成新的列表l5,l5 = ["c"]
l5 = list(li[-1])
print(l5)
# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
l6 = li[-3::-2]
print(l6)

# 3.写代码，有如下列表，按照要求实现每一个功能。

lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

# 将列表lis中的"tt"变成大写（用两种方式）。
lis[3][2][1][0] = lis[3][2][1][0].upper()
print(lis)

lis[3][2][1][0] = 'TT'
print(lis)

# 将列表中的数字3变成字符串"100"（用两种方式）。
# lis[3][2][1][1] = "100"
# print(lis)

lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
print(lis)


# 将列表中的字符串"1"变成数字101（用两种方式）。
# lis[3][2][1][2] = 101
# print(lis)

lis[3][2][1][2] = int(lis[3][2][1][2]) + 100
print(lis)

# 4. 4.请用代码实现：
li = ["alex", "wusir", "taibai"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
value = '_'.join(li)
print(value)

 # 5.利用for循环和range打印出下面列表的索引。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

for i in range(len(li)):
    print(i, end=' ')
print()
# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
# li = list()
# for i in range(100):
#     if i % 2 == 0:
#         li.append(i)
# print(li)

# 切片步长
li = [i for i in range(100)][::2]
print(li)

li = [i for i in range(100) if i % 2 == 0]
print(li)

# 7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
# li = list()
# for i in range(50):
#     if i % 3 == 0:
#         li.append(i)
# print(li)

li = [i for i in range(50)][::3]
print(li)
li = [i for i in range(50) if i % 3 == 0]
print(li)

# 8.利用for循环和range从100~1，倒序打印。
for i in range(100, 0, -1):
    print(i, end= ' ')
print()

# 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
li = list()
for i in range(100, 9, -1):
    if i % 2 == 0 :
        li.append(i)
li = [i for i in li if i % 4 == 0]
print(li)
# 10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。

li = []
for i in range(1, 31):
    li.append(i)
for i in range(len(li)):
    if li[i] % 3 == 0:
        li[i] = '*'
print(li)

