from task6 import get_combinations as g_c


def test_1():
    res = g_c("plan", 2)
    assert res == ["a", "l", "n", "p", "al", "an", "ap", "ln", 
                   "lp", "np"]


def test_2():
    res = g_c("da1", 3)
    assert res == ['1', 'a', 'd', '1a', '1d', 'ad', '1ad']
