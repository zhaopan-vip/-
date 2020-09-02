#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/19 11:55
@desc: 给定两个序列，判定第一个是不是第二个的子序列。（LeetCode 链接如下：https://leetcode.com/problems/is-subsequence/ ）
"""


from collections import Iterable


def is_sub_sequence(a: Iterable, b: Iterable) -> bool:
    c = iter(b)

    gen = ((i in c, i) for i in a)
    print(gen)
    for _, i in gen:
        print("i: {}, in c = {}".format(i, _))
        if not _:
            # 此时 next(c) 已经抛出异常 StopIteration，再执行 i in c 实际上直接返回 False
            return False

    return True


def is_sub_sequence2(a: Iterable, b: Iterable) -> bool:
    b = iter(b)
    return all(i in b for i in a)


if __name__ == '__main__':
    assert is_sub_sequence([1, 3, 5], [1, 2, 3, 4, 5]) is True
    assert is_sub_sequence([1, 4, 3, 2], [1, 2, 3, 4, 5]) is False
