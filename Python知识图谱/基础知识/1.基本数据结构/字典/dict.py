#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/13 10:18
@desc: dict 字典 - python3.6 key 不保证有序，python3.7以上键值有序
"""


# https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries
# 字典的 key 一般是 immutable 类型，例如 strings, numbers, or tuples(此时元组元素也应不可变)
# 字典初始化的几种方式
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
assert d1 == d2 == d3 == d4
# 思考上述几种方式的效率，哪一种最快？
# https://docs.python.org/3/library/dis.html#module-dis
# dis 工具，可以将 CPython 代码进行反编译分析
# d1 > d2 > d4 > d3 ? 猜测 d2 直接由 map 对象创建，可能会比 d4 要快，如果 d4 需要创建 map 对象的话
"""
# python3 -m timeit -n 1000000 "d = {'name': 'jason', 'age': 20, 'gender': 'male'}"
1000000 loops, best of 3: 0.106 usec per loop
# python3 -m timeit -n 1000000 "d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})"
1000000 loops, best of 3: 0.366 usec per loop
# python3 -m timeit -n 1000000 "d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])"
1000000 loops, best of 3: 0.652 usec per loop
python3 -m timeit -n 1000000 "d4 = dict(name='jason', age=20, gender='male')"
1000000 loops, best of 3: 0.311 usec per loop
"""
# d1 > d4 > d2 > d3 这里对d2和d4的推断有错误？
"""
>>> import dis
>>> def f1():
...     return {'name': 'jason', 'age': 20, 'gender': 'male'}
... 
>>> dis.dis(f1)
  2           0 LOAD_CONST               1 ('jason')
              2 LOAD_CONST               2 (20)
              4 LOAD_CONST               3 ('male')
              6 LOAD_CONST               4 (('name', 'age', 'gender'))
              8 BUILD_CONST_KEY_MAP      3
             10 RETURN_VALUE
>>> def f2():
...     return dict({'name': 'jason', 'age': 20, 'gender': 'male'})
... 
>>> dis.dis(f2)
  2           0 LOAD_GLOBAL              0 (dict)
              2 LOAD_CONST               1 ('jason')
              4 LOAD_CONST               2 (20)
              6 LOAD_CONST               3 ('male')
              8 LOAD_CONST               4 (('name', 'age', 'gender'))
             10 BUILD_CONST_KEY_MAP      3
             12 CALL_FUNCTION            1
             14 RETURN_VALUE
>>> def f3():
...     return dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
... 
>>> dis.dis(f3)
  2           0 LOAD_GLOBAL              0 (dict)
              2 LOAD_CONST               7 (('name', 'jason'))
              4 LOAD_CONST               8 (('age', 20))
              6 LOAD_CONST               9 (('gender', 'male'))
              8 BUILD_LIST               3
             10 CALL_FUNCTION            1
             12 RETURN_VALUE
>>> def f4():
...     return dict(name='jason', age=20, gender='male')
... 
>>> dis.dis(f4)
  2           0 LOAD_GLOBAL              0 (dict)
              2 LOAD_CONST               1 ('jason')
              4 LOAD_CONST               2 (20)
              6 LOAD_CONST               3 ('male')
              8 LOAD_CONST               4 (('name', 'age', 'gender'))
             10 CALL_FUNCTION_KW         3
             12 RETURN_VALUE
>>> 

"""
# d4 对应的 f4 函数，比 d2 对应的 f2 函数，要少一个 BUILD_CONST_KEY_MAP 步骤，所以 d4 > d2
# 这里很清晰的看到，kw 并没有拿去创建 key-map 对象，而是 Call——Function——KW 在 C 代码中直接创建的

# 关于字典在python3.6以及3.7版本内部实现变迁的问题，查看源码描述
# https://github.com/python/cpython/blob/3.8/Objects/dictobject.c
