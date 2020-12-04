from task9 import maximize


def test_1():
    lists = [
        [1, 4], 
        [3, 5, 15], 
        [5, 7, 8, 0, 1]
    ]
    assert maximize(lists, m=15) == 14


def test_2():
    lists = [
        [],
        [],
        [],
        []
    ]
    assert maximize(lists, m=9999) == 0


def test_3():
    lists = [
        [-5, 15, 4],
        [-4, -10, -55],
        [-100]
    ]
    assert maximize(lists, 100) == 50
