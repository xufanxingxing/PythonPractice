"""
比如：

A = [[1, 3], [5, 7]]‍‍‌‌‍‌‌‍‌‍‌‍‍‌‍‍‍‌‌
B = [[2, 4], [6, 8]]

要求输出两人共同的空闲时间段。这题返回[[2,3], [6,7]]就好。

答：先记录下每个人的起始时间和结束时间，然后所有时间从左到右扫一遍，记录所有的“两个人都空闲”
的时间段即可。

Follow-up 1: 如果要求共同空闲时间必须超过一定时间（比如，一个小时），怎么办？
答：加一个if判断即可。

Follow-up 2: 如果假设[3, 4]和[4, 5]也有共同空闲时间[4, 4]（可以见一面），怎么办？
答：在每个时间点上，先考虑谁变得available了，处理一下，再考虑谁变得不available了。

Follow-up 3: 如果有20个人，怎么办？
答：用heap。

已顺利拿到onsite。只有这一道题，并不像传说中的必须两道题才能过。但是应该做到bug free了。
求大米！

"""
from queue import PriorityQueue
from functools import cmp_to_key

A = [[1, 3], [5, 7]]
B = [[3, 4], [7, 8]]


def comp(a, b):

    if a[0] == b[0]:
        return a[1] - b[1]
    else:
        return a[0] - b[0]


def commomTime(A, B):

    l = []

    for a in A:
        l.append((a[0], 1))
        l.append((a[1], -1))

    for b in B:
        l.append((b[0], 1))
        l.append((b[1], -1))

    l = sorted(l, key = cmp_to_key(comp))
    print(l)
    count = 0
    currStart = l[0][0]
    res = []
    for time in l:

        if time[1] == 1:
            currStart = time[0]
        else:
            if count == 2:
                res.append([currStart, time[0]])
            currStart = -1
        count += time[1]
    return res

print(commomTime(A, B))





























