#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/18 10:19
@desc: Object Oriented Programming
"""


class A(object):
    """
    类与派生类
    """

    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    """
    继承类
    """

    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    """
    菱形继承
    """

    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B,C):
    """
    观察基类调用顺序
    """

    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')

D()
