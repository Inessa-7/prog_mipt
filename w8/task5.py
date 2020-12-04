from itertools import permutations


def get_permutations(s, n):
    res = sorted(map(lambda x: ''.join(x), permutations(s, r=n)))
    return res

assert get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"]
