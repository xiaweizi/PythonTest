def lazy_sum(*args):
    def sum():
        a = 0
        for i in args:
            a += i
        return a
    return sum

f = lazy_sum(1,2,3,4)
print f()

def count():

    def inner(i):
        return lambda : i * i

    fs = []
    for i in range(1, 4):
        fs.append(inner(i))
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()

# def createCounter():
#     f = [0]
#     def counter():
#         f[0] = f[0] + 1
#         return f[0]
#     return counter

def createCounter():
    f = []
    def counter():
        f.append("")
        return len(f)
    return counter

# def createCounter():
#     def func():
#         n = 0
#         while True:
#             n = n + 1
#             yield n
#     num = func()
#     def counter():
#         return next(num)
#     return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('pass!')
else:
    print('failed!')
