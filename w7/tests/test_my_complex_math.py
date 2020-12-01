from my_mathematics.math import MyComplexMath
import math

def test_sin():
    assert MyComplexMath.sin(2) == math.sin(2)


def test_sqrt():
    res = (-5) ** 0.5
    assert MyComplexMath().sqrt(-5) == (res.real, res.imag)
