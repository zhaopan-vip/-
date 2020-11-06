#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/5 17:42
@desc: 二叉树 binary tree
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


# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/992/
# Pre-order Traversal (先序遍历: 根 - 左子树 - 右子树)
# In-order Traversal (中序遍历: 左子树 - 根 - 右子树)
# Post-order Traversal (后序遍历: 左子树 - 右子树 - 根)
# Recursive or Iterative (递归或者迭代)
# Level-Order traversal (层序遍历: 分解为层级形式遍历所有同层级的节点)


class RecursiveMode:
    """
    通用遍历模式
    """

    @staticmethod
    def pre_order(node: TreeNode, visit_it: callable):
        if node:
            # root - left - right
            visit_it(node.val)
            RecursiveMode.pre_order(node.left, visit_it)
            RecursiveMode.pre_order(node.right, visit_it)

    @staticmethod
    def in_order(node: TreeNode, visit_it: callable):
        if node:
            # left - root - right
            RecursiveMode.in_order(node.left, visit_it)
            visit_it(node.val)
            RecursiveMode.in_order(node.right, visit_it)

    @staticmethod
    def post_order(node: TreeNode, visit_it: callable):
        if node:
            # left - right - root
            RecursiveMode.post_order(node.left, visit_it)
            RecursiveMode.post_order(node.right, visit_it)
            visit_it(node.val)


class IterativeMode:
    """
    使用迭代模式（用栈模拟递归展开，循环遍历）
    """

    @staticmethod
    def level_order(node: TreeNode, visit_it: callable):
        if not node:
            return

        stack = [node]
        while stack:
            # copy
            tmp = []
            while stack:
                top = stack.pop()
                visit_it(top.val)
                # 注意这里加入的顺序
                if top.left:
                    tmp.append(top.left)
                if top.right:
                    tmp.append(top.right)
            stack = tmp[::-1]

    @staticmethod
    def pre_order(node: TreeNode, visit_it: callable):
        if not node:
            return

        # 根 - 左 - 右
        stack = [node]
        while stack:
            top = stack.pop()
            visit_it(top.val)  # 先访问根
            if top.right:
                stack.append(top.right)  # 入栈顺序先右
            if top.left:
                stack.append(top.left)  # 后左

        """
        stack, current = [], node
        while stack or current:
            if current:
                visit_it(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        """

    @staticmethod
    def in_order(node: TreeNode, visit_it: callable):
        if not node:
            return

        # 左 - 根 - 右
        stack, current = [], node
        while stack or current:
            # 将左子树全部入栈
            while current:
                stack.append(current)
                current = current.left
            # 最左节点
            current = stack.pop()
            visit_it(current.val)
            # 如果存在右子树，则右子树入栈
            # 否则回退到其父亲节点
            current = current.right

        """
        stack, current = [], node
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                visit_it(current.val)
                current = current.right
        """

    @staticmethod
    def post_order(node: TreeNode, visit_it: callable):
        if not node:
            return

        # 左 - 右 - 根
        stack, current, prev = [], node, None
        while stack or current:
            # 左子树入栈
            while current:
                stack.append(current)
                current = current.left
            # 最左节点
            current = stack.pop()
            # 查看右子树
            if current.right is None or current.right == prev:
                visit_it(current.val)
                prev = current
                current = None  # 右子树走完了，返回上一层
            else:
                # 右子树存在，重新入栈，当前指针指向右子树
                stack.append(current)
                current = current.right

        """
        stack, current, prev = [], node, None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if current.right is None or current.right == prev:
                    visit_it(current.val)
                    prev = current
                    current = None
                else:
                    stack.append(current)
                    stack.append(current.right)
                    current = current.right.left
        """


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2, right=TreeNode(3))
    root.right = TreeNode(4, left=TreeNode(5))
    root.right.left.left = TreeNode(6, right=TreeNode(7, right=TreeNode(8)))
    root.right.left.right = TreeNode(9)

    pre_order_array = []
    RecursiveMode.pre_order(root, lambda x: pre_order_array.append(x))
    assert pre_order_array == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    in_order_array = []
    RecursiveMode.in_order(root, lambda x: in_order_array.append(x))
    assert in_order_array == [2, 3, 1, 6, 7, 8, 5, 9, 4]

    post_order_array = []
    RecursiveMode.post_order(root, lambda x: post_order_array.append(x))
    assert post_order_array == [3, 2, 8, 7, 6, 9, 5, 4, 1]

    level_order_array = []
    IterativeMode.level_order(root, lambda x: level_order_array.append(x))
    assert level_order_array == [1, 2, 4, 3, 5, 6, 9, 7, 8]

    array_pre_order = []
    IterativeMode.pre_order(root, lambda x: array_pre_order.append(x))
    assert array_pre_order == pre_order_array

    array_in_order = []
    IterativeMode.in_order(root, lambda x: array_in_order.append(x))
    assert array_in_order == in_order_array

    array_post_order = []
    IterativeMode.post_order(root, lambda x: array_post_order.append(x))
    assert array_post_order == post_order_array
