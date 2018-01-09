import functools

int2 = functools.partial(int, base = 2)

print int2('10000')

def func(a, b=2, c=3):
    return a + b + c

func1 = functools.partial(func, b = 0, c = 0)

print func1(1)
