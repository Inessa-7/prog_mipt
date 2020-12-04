def my_zip(*args):
    N = min(map(len, args))
    for i in range(N):
        res = []
        for j in args:
            res.append(j[i])

        yield tuple(res)


def my_map(func, iterable):
    for i in iterable:
        yield func(i)


def my_enumerate(iterable, start=0):
    N = start
    for i in iterable:
        yield N, i
        N += 1


if __name__ == '__main__':
    names = ["Alex", "Bob", "Alice", "John", "Ann"]
    age = [25, 17, 34, 24, 42]
    sex = ["M", "M", "F", "M", "F"]

    for values in my_zip(names, age, sex):
        print("name: {:>10} age: {:3} sex: {:2}".format(*values))
