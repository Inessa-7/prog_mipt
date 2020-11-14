import math


class MyMath:
    pi = 3.14
    _complex = False
    
    @staticmethod
    def sin(x):
        return math.sin(x)

    @classmethod
    def sqrt(cls, x):
        '''
        В данном месте используется полиморфизм, так как в классе-потомке
        меняется поведение метода.
        Классметод используется как раз для этого, потому что он позволяет
        менять поведение метода, используя поле _complex
        '''
        if x < 0:
            if cls._complex:
                res = x ** 0.5
                return (x.real, x.imag)
            else:
                raise ValueError('Koren iz otriz chisla!')
        return x ** 0.5


class MyComplexMath(MyMath): 
    '''
    Здесь используется наследование, так как данный класс использует все
    методы, определенные в классе-родителе. 
    '''
    _complex = True
