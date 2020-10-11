#!/usr/bin/python
def swap(func):
    def wrapper(*args, **kwargs):
        result = func(*args[::-1], **kwargs)
        return result
    return wrapper


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return(res)

div(3, 9, show=True)


