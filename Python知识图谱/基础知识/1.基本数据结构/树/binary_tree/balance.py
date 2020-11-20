#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/20 5:16 PM
"""

from typing import Tuple

from node import TreeNode


def is_balanced(root: TreeNode) -> bool:
    if not root:
        return True

    def dfs(node: TreeNode) -> Tuple[int, bool]:
        """
        遍历返回节点的深度、是否平衡

        :type node: TreeNode
        :rtype: Tuple[int, bool]
        """
        depth_l, balance_l = dfs(node.left) if node.left else (0, True)
        depth_r, balance_r = dfs(node.right) if node.right else (0, True)
        depth = 1 + max(depth_l, depth_r)
        balance = balance_l and balance_r and abs(depth_l - depth_r) <= 1
        return depth, balance

    return dfs(root)[1]


if __name__ == "__main__":
    # test case
    from testcase import BalanceCase
    from serialize import deserialize
    for tc in BalanceCase.TEST:
        root = deserialize(tc[0])
        assert tc[1] == is_balanced(root)
