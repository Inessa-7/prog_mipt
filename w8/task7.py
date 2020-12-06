from itertools import combinations_with_replacement as cwr


def get_combinations_with_r(s, n):
    a1 = list(map(lambda x: sorted(x), cwr(s, n)))
    res = list(map(lambda x: ''.join(x), sorted(a1)))
    return res

assert get_combinations_with_r("cat", 2) == ["aa", "ac", "at", "cc", "ct", "tt"]
