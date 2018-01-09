def sum(a, b):
    return a + b

print sum(1, 2)

bb = sum

print bb(2, 3)

myFunc = lambda x, y : x + y

print myFunc(1, 2)

myFunc = lambda x, y=10 : x + y
print myFunc(12)

myList = [lambda x:x**2, lambda x:x**3, lambda x:x**4]
res2 = myList[1]

print res2(4)
