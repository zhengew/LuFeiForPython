# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: hw.py
# @datatime: 2024/3/7 21:04


# Day2作业及默写

# 1.  # 判断下列逻辑语句的True,False.
#
# 1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# False or True or False and True and True or False
#
# False or True or False and True or False
# False or True or False or False
# True or False or False
# True or False
# True
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # True

# 2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
'''
not True and True or False and True and True or False
False and True or False and True and True or False
False or False and True and True or False
False or False and True or False
False or False or False
False
'''
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # False

# 2.  # 求出下列逻辑语句的值。
# 1), 8 or 3 and 4 or 2 and 0 or 9 and 7
# 8 or 4 or 0 or 7
# 8 or 0 or 7
# 8 or 7
# 8

# print(8 or 3 and 4 or 2 and 0 or 9 and 7) # 8

# 2), 0 or 2 and 3 and 4 or 6 and 0 or 3
# 0 or 3 and 4 or 0 or 3
# 0 or 4 or 0 or 3
# 4 or 0 or 3
# 4 or 3
# 4

# print(0 or 2 and 3 and 4 or 6 and 0 or 3) # 4

# 3.  # 下列结果是什么？

# 1)、6 or 2 > 1
# 6 or True
# 6
# print(6 or 2 > 1) # 6

# 2)、3 or 2 > 1
# 3 or True
# 3

# print(3 or 2 > 1) # 3


# 3)、0 or 5 < 4
'''
0 or False
False
'''
# print(0 or 5 < 4) # False

# 4)、5 < 4 or 3
'''
False or 3
3
'''
# print(5<4 or 3) # 3

# 5)、2 > 1 or 6
'''
True or 6
True
'''
# print(2>1 or 6) # True

# 6)、3 and 2 > 1
'''
3 and True
True
'''
# print(3 and 2 > 1) # True
# 8)、2 > 1 and 3
'''
True and 3
3
'''
# print(2 > 1 and 3) # 3
# 9)、3 > 1 and 0
'''
True and 0
0
'''
# print(3 > 1 and 0) # 0

# 10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# True and 2 or False and 3 and 4 or True
# 2 or False and 4 or True
# 2 or False or True
# 2 or True
# 2

# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2) # 2

# 4.  # while循环语句基本结构？
'''
while 循环条件:
    循环体
'''
# 5.  # 利用while语句写出猜大小的游戏：
# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;
# 只有等于66，显示猜测结果正确，然后退出循环。
# lucky_number = 66
# while True:
#     guess_number = input('请输入数字：>>>\n')
#     if not guess_number.isdecimal():
#         print('请输入数字~')
#         continue
#     guess_number = int(guess_number)
#     if guess_number == lucky_number:
#         print('猜测结果正确')
#         break
#     elif guess_number > lucky_number:
#         print('猜大了')
#     elif guess_number < lucky_number:
#         print('猜小了')

# 6.  # 在5题的基础上进行升级：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘太笨了你....’。
# lucky_number = 66
# guess_time = 3
# while guess_time >= 1:
#     guess_number = input('请输入数字：>>>\n')
#     guess_time -= 1
#     if not guess_number.isdecimal():
#         print('请输入数字~')
#         continue
#     guess_number = int(guess_number)
#     if guess_number == lucky_number:
#         print('猜测结果正确')
#         break
#     elif guess_number > lucky_number:
#         print('猜大了')
#     elif guess_number < lucky_number:
#         print('猜小了')
#
# else:
#     print('太笨了你')

# 7.  # 使用while循环输出 1 2 3 4 5 6 8 9 10
# n = 1
# while n < 11:
#     if n != 7:
#         print(n, end=' ')
#     n += 1

# 8.求1 - 100的所有数的和
# n = 1
# res = 0
# while n <= 100:
#     res += n
#     n += 1
# print(res)

# 9.  # 输出 1-100 内的所有奇数
# n = 1
# while n <= 100:
#     if n % 2 != 0:
#         print(n, end=' ')
#     n += 1

# 10.  # 输出 1-100 内的所有偶数
# n = 1
# while n <= 100:
#     if n % 2 == 0:
#         print(n, end=' ')
#     n += 1

# 11.  # 求1-2+3-4+5 ... 99的所有数的和
# count = 1
# res = 0
# while count < 100:
#     if count % 2 == 0:
#         res -= count
#     else:
#         res += count
#     count += 1
# print(res) # 50
# 12.  # 用户登录（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
#

# 13.  # 简述ASCII、Unicode、utf-8编码
#
# ASCII：只包含英文字母，数字，特殊字符。均占8位（1
# 字节）
#
# Unicode：万国码，包括世界上所有的文字，不论中文、英文或符号，每个字符均占32位（4
# 字节）。浪费空间，浪费资源。
#
# utf - 8：万国码升级版，英文占8位（1
# 字节）、欧洲字符占16位（2
# 字节）、中文字符站24位（3
# 字节）

# 14.  # 简述位和字节的关系？
#
# 8位 = 1字节

