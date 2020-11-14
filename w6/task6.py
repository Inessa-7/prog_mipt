import math


class Complex:
    def __init__(self, x, y):
        self.real = x
        self.imag = y

    def __abs__(self):
        res = (self.real ** 2 + self.imag ** 2) ** 0.5
        return res

    def __add__(self, obj):
        return Complex(self.real + obj.real, self.imag + obj.imag)

    def __sub__(self, obj):
        return Complex(self.real - obj.real, self.imag - obj.imag)
    
    def __mul__(self, obj):
        real = self.real * obj.real - self.imag * obj.imag
        imag = self.real * obj.imag + self.imag * obj.real
        return Complex(real, imag)
    
    def __truediv__(self, obj):
        a, b = self.real, self.imag
        c, d = obj.real, obj.imag
        real = (a * c + b * d) / (c ** 2 + d ** 2)
        imag = (b * c - a * d) / (c ** 2 + d ** 2)
        return Complex(real, imag)
    
    def __neg__(self):
        return Complex(-self.real, -self.imag)
    
    def __pow__(self, n):
        r = abs(self)
        fi = math.atan(self.imag / self.real)
        real = r ** n * math.cos(fi * n)
        imag = r ** n * math.sin(fi * n)
        return Complex(real, imag)

    def __repr__(self):
        if self.imag < 0:
            return '{}{}i'.format(self.real, self.imag)
        else:
            return '{}+{}i'.format(self.real, self.imag)


if __name__ == '__main__':
    a = Complex(3, 3)
    b = Complex(1, 1)
    print(a)
    print(a + b)
    print(a - b)
    print(-a)
    print(a * b)
    print(abs(a))
    print(a / b)
    print(a ** 5)
