#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/20 2:25 PM
"""

from typing import Mapping

from binary_tree import TreeNode


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root or distance <= 1:
            return 0

        def dfs(node: TreeNode) -> Mapping[int, int]:
            assert node is not None

            # terminator
            if node.left is None and node.right is None:
                # 叶子
                return {1: 1}

            ld = dfs(node.left) if node.left else {}
            rd = dfs(node.right) if node.right else {}

            for l in ld:
                for r in rd:
                    if l + r <= distance:
                        nonlocal res
                        res += ld[l] * rd[r]

            # 计算本节点，子树深度+1，同深度数量进行合并
            s = {}
            for l in sorted(ld.keys()):
                if l >= distance:
                    break
                s[l+1] = ld[l]
            for r in sorted(rd.keys()):
                if r >= distance:
                    break
                if r+1 not in s:
                    s[r+1] = rd[r]
                else:
                    s[r+1] += rd[r]
            return s

        res = 0
        dfs(root)
        return res


        # 阅读题目
        # 二叉树
        # 两个叶子节点之间的最短路径 <= distance
        # 返回总的路径数量
        # 思路
        # 最短路径为最小的公共祖先根节点，和层高有关
        # 任务分解
        # 1、当前根节点进行左右配对
        # 2、递归到左、右子树
        # 针对任务1继续分解
        # 1.1 统计左子树深度、以及深度计数，同理右子树
        # depth-l 集合任选 i + depth-r 集合任选 j + 2 <= distance 为当前任务1的解
        # 设计递归过程，返回其深度对应的叶子数量，同时可以计算total


if __name__ == '__main__':
    s = """[61,46,16,61,49,93,12,92,44,4,69,56,25,92,6,10,39,59,93,39,5,72,12,16,31,5,54,75,62,null,null,31,79,10,null,81,93,null,null,2,47,100,65,68,null,97,null,60,87,80,null,36,null,null,null,21,11,null,55,98,50,1,51,87,null,51,73,68,null,15,38,10,null,100,61,52,null,null,null,null,null,52,6,29,null,63,null,37,11,null,56,null,null,null,null,95,83,null,null,37,29,null,null,null,null,68,45,91,null,24,null,36,null,28,null,null,null,null,null,84,null,null,null,60,21,null,null,64,54,38,null,45,null,null,null,null,null,92,null,51,45,100,null,null,null,81,null,null,37,34,null,null,97,74,null,null,null,null,null,6,null,9,null,null,50,null,null,null,50,null,36,80,7,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,null,32,71,null,null,null,null,37,7,null,28]"""
    a = 5
    b = 38
    from binary_tree.serialize import deserialize

    root = deserialize(s)
    result = Solution().countPairs(root, a)
    print(result)
    assert result == b
