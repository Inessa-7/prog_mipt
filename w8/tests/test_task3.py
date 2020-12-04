from task3 import my_zip, my_map, my_enumerate


def test_zip_1():
    res1 = list(my_zip([1, 2], [3, 4]))
    res2 = list(zip([1, 2], [3, 4]))
    assert res1 == res2


def test_zip_2():
    res1 = list(my_zip([1, 2, 3], ('a', 'b')))
    res2 = list(zip([1, 2, 3], ('a', 'b')))


def test_map_1():
    res1 = list(my_map(lambda x: x ** 2, range(1, 100)))
    res2 = list(map(lambda x: x ** 2, range(1, 100)))
    assert res1 == res2


def test_map_2():
    res1 = list(my_map(int, ['1', '2', '3']))
    res2 = list(map(int, ['1', '2', '3']))
    assert res1 == res2


def test_enum_1():
    res1 = list(my_enumerate(['a', 'b', 'c']))
    res2 = list(enumerate(['a', 'b', 'c']))
    assert res1 == res2


def test_enum_2():
    res1 = list(my_enumerate([1, 2, 5], start=5))
    res2 = list(enumerate([1, 2, 5], start=5))
    assert res1 == res2
