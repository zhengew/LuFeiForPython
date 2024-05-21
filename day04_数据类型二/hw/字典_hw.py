# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 字典_hw.py
# @datatime: 2024/5/14 19:38
# 1.
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,
# 将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
li= [11,22,33,44,55,66,77,88,99,90]
data = dict.fromkeys(['greater', 'less'], [])
print(data) # {'greater': [], 'less': []}

data.update(greater=[i for i in li if i > 66], less=[i for i in li if i < 66])
print(data) # {'greater': [77, 88, 99, 90], 'less': [11, 22, 33, 44, 55]}


# 2.有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
info = "k: 1|k1:2|k2:3 |k3 :4"
res = dict()
for i in info.split('|'):
    key, value = i.replace(' ', '').split(':')
    # res[key] = int(value)
    res.update([(key, value)])
print(res)

# 3.请循环打印k2对应的值中的每个元素

info = {
    'k1':'v1',
    'k2':[('alex'),('wupeiqi'),('oldboy')],
}

for i in info['k2']:
    print(i)
