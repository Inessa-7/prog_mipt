def my_coroutine():
    while True:
        x = yield
        mean = 0
        for i in x:
            mean += i
        mean /= len(x)
        disp = 0
        for i in x:
            disp += (i - mean) ** 2
        disp /= (len(x) - 1)
        print('Srednee:', mean)
        print('Dispersia:', disp)
        print('Kol-vo:', len(x))


if __name__ == '__main__':
    cor = my_coroutine()
    next(cor)
    cor.send([1, 2, 3])
    cor.send([5, 5, 5])
