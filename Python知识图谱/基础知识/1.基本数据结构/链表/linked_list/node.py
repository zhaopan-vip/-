#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/25 3:25 PM
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class DoubleListNode(ListNode):

    def __init__(self, val):
        super().__init__(val)
        self.prev = None
