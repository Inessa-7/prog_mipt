#!/usr/bin/python
def my_dec(func):
    def wrapper(my_list):
        n = func(my_list)
        if n == 0:
            return 'Нет('
        elif n > 10:
            return 'Очень много'
    return wrapper


@my_dec
def count_even(my_list):
    N = 0 
    for i in my_list:
        if i % 2 == 0:
            N += 1
    return N

print(count_even([1, 3, 5, 7, 9]))


