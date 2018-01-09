# -*- coding: utf-8 -*-

import functools,time

def sum():
    print 'sum'

print sum.__name__


def log(func):
    @functools.wraps(func)
    def wrapper(*args):
        return func(*args) + 1
    return wrapper

@log
def now(x):
    return x * x

print now.__name__

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **k):
        start = time.clock()
        fun = fn(*args, **k)
        end = time.clock()
        duration = end - start
        print('%s executed in %s ms' % (fn.__name__, duration))
        return fun
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print '测试成功'
