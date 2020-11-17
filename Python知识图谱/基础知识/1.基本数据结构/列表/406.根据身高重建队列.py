#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/11/16 11:09 AM
"""


def reconstructQueue(people: list) -> list:
    if not people or len(people) == 1:
        return people
    return hk_order(people)


def hk_order(people: list) -> list:
    # h升序 k降序
    people.sort(key=lambda x: (x[0], -x[1]))
    # 找到最矮的位置
    res, index_res = [[0,0] for i in range(len(people))], [i for i in range(len(people))]
    for h,k in people:
        # k 值就是索引
        val = index_res.pop(k)
        res[val] = [h, k]
    return res


def full_traversor(people: list):
    s = set([(h,k) for h,k in people])

    def check(array, element):
        count = 0
        for item in array:
            if item[0] >= element[0]:
                count += 1
        if count == element[1]:
            return True
        return False

    def check_dict(data, element):
        keys = list(data.keys())
        keys.sort()
        import bisect
        idx = bisect.bisect_left(keys, element[0])
        count = 0
        for i in range(idx, len(keys)):
            count += data[keys[i]]
        return count == element[1]

    def dfs(src, dest, dest_dict, n, res):
        # terminator
        if len(dest) == n:
            res.extend(dest)
            return False
        # 遍历剩余的元素，判断是否符合队列排序
        # 放入res队列的元素，肯定是符合条件的，主要是判断src的元素遍历
        s1 = set(src)
        for item in src:
            if not check_dict(dest_dict, item):
                continue
            dest.append([item[0], item[1]])
            count = dest_dict.get(item[0], 0)
            dest_dict[item[0]] = count + 1
            # 进入下一层
            s1.discard(item)
            ret = dfs(s1, dest, dest_dict, n, res)
            if not ret:
                return False
            s1.add(item)
            dest.pop(-1)
            dest_dict[item[0]] = count
            if count == 0:
                del dest_dict[item[0]]
        return True

    dest, dest_dict, res = [], {}, []
    dfs(s, dest, dest_dict, len(people), res)
    return res

if __name__ == '__main__':
    result = reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    print(result)
    assert result == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

    a = [[40,11],[81,12],[32,60],[36,39],[76,19],[11,37],[67,13],[45,39],[99,0],[35,20],[15,3],[62,13],[90,2],[86,0],[26,13],[68,32],[91,4],[23,24],[73,14],[86,13],[62,6],[36,13],[67,9],[39,57],[15,45],[37,26],[12,88],[30,18],[39,60],[77,2],[24,38],[72,7],[96,1],[29,47],[92,1],[67,28],[54,44],[46,35],[3,85],[27,9],[82,14],[29,17],[80,11],[84,10],[5,59],[82,6],[62,25],[64,29],[88,8],[11,20],[83,0],[94,4],[43,42],[73,9],[57,32],[76,24],[14,67],[86,2],[13,47],[93,1],[95,2],[87,8],[8,78],[58,16],[26,75],[26,15],[24,56],[69,9],[42,22],[70,17],[34,48],[26,39],[22,28],[21,8],[51,44],[35,4],[25,48],[78,18],[29,30],[13,63],[68,8],[21,38],[56,20],[84,14],[56,27],[60,40],[98,0],[63,7],[27,46],[70,13],[29,23],[49,6],[5,64],[67,11],[2,31],[59,8],[93,0],[50,39],[84,6],[19,39]]
    b = reconstructQueue(a)
    print(b)
