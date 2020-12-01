import pytest
from my_mathematics.math import MyMath
import math


def test_sin():
    for i in [0, 0.5, 3.14]:
        assert MyMath.sin(i) == math.sin(i)


def test_neg_sqrt():
    with pytest.raises(ValueError):
        MyMath().sqrt(-1)


def test_sqrt():
    assert math.sqrt(2) == MyMath().sqrt(2)
