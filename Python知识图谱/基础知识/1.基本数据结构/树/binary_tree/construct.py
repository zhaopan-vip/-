#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/23 4:52 PM
@desc: 构造二叉树
"""

from typing import List
from node import TreeNode


class Construct:

    @staticmethod
    def from_pre_post(pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None

        root = TreeNode(pre[0])

        # 左右边界判定
        if len(pre) == 1:
            return root

        left_val = pre[1]
        left_count = post.index(left_val) + 1

        root.left = Construct.from_pre_post(pre[1:left_count+1], post[0:left_count])
        root.right = Construct.from_pre_post(pre[left_count+1:], post[left_count:-1])

        return root

if __name__ == '__main__':
    pass
