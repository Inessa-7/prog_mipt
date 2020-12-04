def print_map(function, iterable):
    for i in iterable:
        print(function(i))


def my_map(function, iterable):
    res = list(map(function, iterable))
    print(*res, sep='\n')


print_map(lambda x: x ** 2, [i for i in range(1, 10)])
my_map(lambda x: x**2, [i for i in range(1, 10)])
