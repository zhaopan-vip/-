#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/13 10:02
@desc: tuple 元组 immutable
"""


# https://docs.python.org/3.6/tutorial/datastructures.html#tuples-and-sequences
# 元组和序列化类型（list, tuple, range)
empty = ()                  # empty
singleton = ('hello', )     # <-- note trailing comma
t = 12345, 54321, 'hello!'
x, y, z = t                 # an example of tuple packing
assert x == t[0]
assert y == t[1]
assert z == t[2]
t += ('world',)             # create a new tuple
assert t == ('hello', 'world')
