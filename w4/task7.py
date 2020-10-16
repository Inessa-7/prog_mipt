#!/usr/bin/python

from datetime import datetime


def logger(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t1 = datetime.now()
            result = func(*args, **kwargs)
            t2 = datetime.now()
            t3 = t2 - t1
            with open(filename, 'w') as f:
                f.write(str(t1) + '\n')
                f.write(' '.join(map(str, args)) + '\n') 
                if result:
                    f.write(str(result) + '\n')
                else:
                    f.write('-\n')
                f.write(str(t2) + '\n')
                f.write(str(t3) + '\n')
            return result
        return wrapper
    return decorator


@logger('ans_task7.txt')
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return(res)


div(3, 9, show=True)

