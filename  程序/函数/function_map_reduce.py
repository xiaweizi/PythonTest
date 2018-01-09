# -*- coding: utf-8 -*-

myFunc = lambda x : x * x
L = range(0, 10)

# 第一个参数传入函数，第二个参数传入 Iterable
B = map(myFunc, L)
print B

def func(x):
    return x + x

C = list(map(func, L))
print C

# reduce
A = range(0, 10)
func1 = lambda x, y : x + y
print reduce(func1, A)

def func2(x):
    if x == 1:
        return 1
    list1 = range(1, x)
    func = lambda x, y :x * y
    return reduce(func, list1)

for value in range(1, 11):
    print func2(value)


def func3(x):
    return int(x)


def func4(x, y):
    return x * 5 + y
str = '323424'
L = reduce(func4, map(func3, str))
print str
print L

def func5(x):
    value = x.lower()
    return value.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(func5, L1))
print L2

# 测试乘积

func7 = lambda x, y : x * y

def prod(L):
    return reduce(func7, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    return float(s)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

def myFunc1(x):
    for index,value in enumerate(x):
        if value == '.':
            return index

fun1 = lambda x, y : x * 10 + y
fun2 = lambda x, y : y * 0.1 + y

def myFunc2(x):
    index = myFunc1(x)
    start = x[:index]
    end = x[index+1:]
    print reduce(fun1, str(start))
    print reduce(fun2, str(end))

myFunc2('12.22')
