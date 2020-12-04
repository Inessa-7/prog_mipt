from task4 import get_cartesian_product


def test_1():
    res =  get_cartesian_product([5, 6], [8, 9]) 
    assert res == [(5,8),(5,9),(6,8),(6,9)]


def test_2():
    res = get_cartesian_product(['a', 'c'], [1, 2, 5])
    assert res == [('a', 1), ('a', 2), ('a', 5), ('c', 1), ('c', 2), ('c', 5)]
