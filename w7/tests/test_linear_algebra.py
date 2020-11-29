from my_mathematics.linear_algebra import Vector


def test_abs():
    assert abs(Vector('1,1,1')) == 3 ** 0.5


def test_add():
    assert Vector('1,1,1') + Vector('1,1,1') == Vector('2,2,2')


def test_sub():
    assert Vector('1,1,1') - Vector('1,1,1') == Vector('0,0,0')


def test_mul():
    assert Vector('1,1,1') * Vector('1,1,1') == 3


def test_vec_mul():
    assert Vector('1,0,0') & Vector('0,1,0') == Vector('0,0,1')

