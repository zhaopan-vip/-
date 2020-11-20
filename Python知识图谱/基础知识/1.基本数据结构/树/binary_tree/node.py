#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/20 4:36 PM
"""


class TreeNode:
    """
    Define Binary Tree Node Structure
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'val={}'.format(self.val)
