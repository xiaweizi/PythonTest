# -*- coding: utf-8 -*-


# 返回 0 - 10 之间的偶数
# print filter(lambda x : x % 2 == 0, range(0, 11))

# 判断一个整数是否是质数
def _zhishu(value):
    if value < 2:
        pass
    for x in range(2, value):
        if value % x == 0:
            return False
    return True
# print filter(_zhishu, range(2, 101))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for i in primes():
    print(i)
    if i >= 152:
        print(i)
        break
