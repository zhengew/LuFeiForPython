# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 代码块.py
# @datatime: 2024/3/18 22:44

# id is == 区别
# 1. id(__obj)  # 获取对象的内存地址
print(id('alex')) # 4462300400

# 2. is    # 比较对象的内存地址是否相等
a = 'alex'
b = 'alex'
res = a is b
print(res, f'变量a的内存地址:{id(a)}, 变量b的内存地址:{id(b)}') # True 变量a的内存地址:4429892848, 变量b的内存地址:4429892848

# 3. ==   # 比较 值是否相等
a = 'alex'
b = 'alex'
res = a == b
print(res) # True

# 结论： == 比较值是否相等，is 比较内存地址是否相等，如果内存地址相同，值肯定相等；如果值相等，内存地址不一定相同