from itertools import groupby


def compress_string(s):
    res = []
    for k, g in groupby(s):
        res.append((len(list(g)), k))
    return res

assert compress_string('1222311') == [(1, '1'), (3, '2'), (1, '3'), (2, '1')]
