from itertools import product


def maximize(lists, m):
    res = 0
    for i in product(*lists):
        s = 0
        for j in i:
            s += j * j
        if s % m > res:
            res = s % m
    return res

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
assert maximize(lists, m=1000) == 206
