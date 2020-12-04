from itertools import combinations


def get_combinations(s, n):
    res = []
    for i in range(1, n + 1):
        a1 = list(combinations(s, i))
        a2 = sorted(list(map(lambda x: sorted(x), a1)))
        res += list(map(lambda x: ''.join(x), a2))
    return res

assert get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"]
