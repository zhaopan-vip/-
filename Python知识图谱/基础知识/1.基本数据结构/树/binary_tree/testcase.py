#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/20 5:21 PM
"""


class TestCase:
    pass


class BalanceCase(TestCase):
    TEST = [
        ('[3,9,20,null,null,15,7]', True),
        ('[1,2,2,3,3,null,null,4,4]', False)
    ]
