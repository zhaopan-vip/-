#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/20 4:37 PM
"""

from node import TreeNode


def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return "[]"
    # level order
    stack, res = [root], []
    while stack:
        array = []
        for _ in range(len(stack)):
            # FIFO
            top = stack.pop(0)
            if not top:
                array.append(None)
                continue
            array.append(top.val)
            stack.append(top.left)
            stack.append(top.right)
        if all([val is None for val in array]):
            break
        # print(array)
        res.append(array)
    # make str
    s = []
    for level_nodes in res:
        for val in level_nodes:
            if val is None:
                s.append("null")
            else:
                s.append(str(val))
    content = ",".join(s)
    return "[%s]" % content


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if not data or data[0] != "[" or data[-1] != "]":
        return None
    if len(data) == 2:
        return None
    s = data[1:-1].split(',')
    # print(s)
    root, level, level_nodes = None, 0, []
    res = []
    for val in s:
        # every val means a node or None
        node = None
        if val == "null":
            node = None
        else:
            try:
                node = TreeNode(int(val))
                node.write = 0
            except:
                pass
        # print(node)
        if level == 0:
            # root
            root = node
            level += 1
            level_nodes = []
            res.append([root])
        else:
            # append node to last level parents
            last_level_nodes = res[level - 1]
            saved = False
            for item in last_level_nodes:
                if item is None:
                    continue
                if item.write == 0:
                    item.left = node
                    item.write = 1
                    saved = True
                    break
                if item.write == 1:
                    item.right = node
                    item.write = 2
                    saved = True
                    break
            if saved:
                level_nodes.append(node)
            is_full = False
            for i in range(len(last_level_nodes) - 1, -1, -1):
                if last_level_nodes[i] is None:
                    continue
                if last_level_nodes[i].write == 2:
                    is_full = True
                break
            if is_full:
                # enter next level
                res.append(level_nodes)
                level += 1
                level_nodes = []
    return root


if __name__ == '__main__':
    s = "[1,2,3,null,null,4,5]"
    root = deserialize(s)
    assert s == serialize(root)
