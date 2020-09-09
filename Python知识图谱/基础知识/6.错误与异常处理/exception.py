#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/9/3 15:09
"""


items = []
try:
    items.append(1)
    raise Exception('xxx')
except:
    print(items)
finally:
    items.clear()

print(items)
