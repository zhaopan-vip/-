#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/24 2:58 PM
"""

from binary_tree.node import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.iteractive(root)

    def iteractive(self, root: TreeNode) -> int:
        # 用迭代方式展开下面的递归函数
        current, count = root, 0
        while current:
            depth_left = self.height(current.left)
            depth_right = self.height(current.right)

            if depth_right == depth_left:
                # 当前节点左子树是满二叉树，跳转到右子树
                current = current.right
                count += 1 << depth_right
            else:
                # 当前节点右子树是满二叉树，跳转到左子树
                current = current.left
                count += 1 << depth_right
        return count

    def recursive(self, root: TreeNode) -> int:
        # 采用左子树来进行二分递归
        depth = self.height(root)
        if depth <= 1:
            return depth

        # 右子树深度 + 1 = 整棵树的深度
        depth_right = self.height(root.right)
        if depth_right == depth - 1:
            # 意味着左子树是满二叉树，递归计算右子树，然后合并
            return 2**depth_right + self.recursive(root.right)
        else:
            # 意味着右子树是满二叉树，递归计算左子树，合并
            return 2**depth_right + self.recursive(root.left)

    def height(self, node: TreeNode) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth
