#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/13 11:55
@desc: set 集合
"""


# https://docs.python.org/3.6/tutorial/datastructures.html#sets
# 集合
s = {1, 2, 3}
s.add(4)        # 增加元素
s.remove(4)     # 删除元素

# 排序
s_sorted = sorted(s)

# 查找
assert 1 in s

# 运算符
a = set('abracadabra')
b = set('alacazam')
_ = a - b
_ = a | b
_ = a & b
_ = a ^ b

# comprehensions 推导
s = {x for x in a if x not in b}
print(s)
