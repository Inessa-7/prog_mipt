def c():
    raise ValueError('my exception')


def b():
    c()


def a():
    b()


a()
