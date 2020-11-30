#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/26 11:41 AM
"""

import math


def radix_sort(nums, radix=10):
    """nums为整数列表， radix为基数"""

    # 最大位数
    K = int(math.ceil(math.log(max(nums), radix))) + 1
    # 构造桶的容器
    bucket = [[] for i in range(radix)]

    # 从低位开始比较 LSD: Least Significant Digit first
    for i in range(1, K + 1):
        for val in nums:
            index = (val % radix ** i) // (radix ** (i - 1))
            bucket[index].append(val)
        # 组装桶元素，写回nums
        count = 0
        for sub in bucket:
            for val in sub:
                nums[count] = val
                count += 1
            sub.clear()


if __name__ == '__main__':
    array = [1, 10**1]
    radix_sort(array)
    print(array)
