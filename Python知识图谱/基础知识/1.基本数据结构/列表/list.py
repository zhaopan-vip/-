#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/12 17:12
@desc: list 列表
"""


# https://docs.python.org/3.6/tutorial/introduction.html#lists
# 列表常见操作
l = [1, 2, 3, 4, 5]
l = list(l)
# 切片(slice)
l = l[:]        # new (shallow) copy of the list
l = l[::-1]     # revers of the list
print(l[-1])    # 负数索引
