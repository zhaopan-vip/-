#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/17 11:25 AM
"""


# Define Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_dst(self):
        return abs(self.x) + abs(self.y)

    def translate(self, a, b):
        return [self.x + a, self.y + b]

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Rectangle:
    def __init__(self, left_top, right_bottom):
        self.pt_start = left_top
        self.pt_end = right_bottom
        # 另外两个顶点
        self.pt_start2 = Point(left_top.x, right_bottom.y)
        self.pt_end2 = Point(right_bottom.x, left_top.y)

    def calculate_max_dst(self):
        # 即四个顶点到原点的最大距离
        points = [self.pt_start, self.pt_end, self.pt_start2, self.pt_end2]
        return max([pt.calculate_dst() for pt in points])

    def check_in_rectangle(self, pt):
        return self.pt_start.x <= pt.x <= self.pt_end.x and self.pt_start.y <= pt.y <= self.pt_end.y


class Solution:

    def __init__(self):
        pass

    def all_cells_dist_order(self, r: int, c: int, r0: int, c0: int) -> list:
        assert 1 <= r <= 100 and 1 <= c <= 100
        assert 0 <= r0 < r and 0 <= c0 < c

        # 坐标变换
        left_top, right_bottom = Point(-r0, -c0), Point(r - 1 - r0, c - 1 - c0)
        rc = Rectangle(left_top, right_bottom)
        # 计算最大距离
        dst = rc.calculate_max_dst()
        # 进行转圈 0 to dst
        res = []
        for i in range(dst + 1):
            # 注意优化遍历方式，超出矩形区域的部分
            if i == 0:
                pt = Point(0, 0)
                res.append(pt.translate(r0, c0))
                continue
            # X轴 Y轴 一二三四象限对称的
            # (n, 0) -> (0, n) -> (-n, 0) -> (0, -n)
            for k in range(0, i + 1):
                # print(i, k)
                pt = Point(k, i - k)
                points = [pt, ]
                # 对称的点
                if pt.x != 0:
                    points.append(Point(-pt.x, pt.y))
                if pt.y != 0:
                    points.append(Point(pt.x, -pt.y))
                if pt.x != 0 and pt.y != 0:
                    points.append(Point(-pt.x, -pt.y))
                # print(points)

                # 过滤
                points = [pt.translate(r0, c0) for pt in points if rc.check_in_rectangle(pt)]
                # print(points)
                if points:
                    res.extend(points)
        return res

# 思路
# 直观想法是不要排序，以(r0,c0)坐标为原点，进行辐射
# 矩阵通过坐标变换得到(0, 0) ~ (r-1, c-1) 变换为 (-r0, -c0) ~ (r-1-r0, c-1-c0)
# 围绕着原点，进行转圈输出
# dst = 0 [0, 0]
# dst = 1 [1, 0], [0, 1], [-1, 0], [0, -1]
# dst = 2 [2, 0], [1, 1], [0, 1], [-1, -1], [-2, 0], [-1, -1], [0, -2], [1, -1]
# dst = 3 ...
# dst = n [n, 0], [n-1, 1], [n-2, 2]...[0, n], [-1, n-1], [-2, n-2]...[-n, 0], [-(n-1), -1]...[0, -n]...
# 对结果进行过滤，然后坐标转换回来输出
# 确认最大距离为四个顶点到原点的距离


if __name__ == '__main__':
    # print(Solution().all_cells_dist_order(1, 2, 0, 0))
    print(Solution().all_cells_dist_order(2, 2, 0, 1))
    # print(Solution().all_cells_dist_order(2, 3, 1, 2))
