def func(x):
    return x

L = map(func, range(0, 11))

print list(L)

def func1(x, y):
    print x, y

B = reduce(func1, range(0, 11))

print B


def fun(x):
    print x

print filter(fun, range(1, 11))
