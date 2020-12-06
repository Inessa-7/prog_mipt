from task2 import fib


def test_fib_1():
    assert list(fib(5)) == [0, 1, 1, 2, 3]


def test_fib_2():
    assert list(fib(8)) == [0, 1, 1, 2, 3, 5, 8, 13]
