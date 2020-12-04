from task8 import compress_string as c_s


def test_1():
    res = c_s('323321124ggbbsa')
    assert res == [(1, '3'), (1, '2'), (2, '3'), (1, '2'), (2, '1'),
                   (1, '2'), (1, '4'), (2, 'g'), (2, 'b'), (1, 's'), 
                   (1, 'a')]


def test_2():
    res = c_s('')
    assert res == []
