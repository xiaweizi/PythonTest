def func(a):
    if a == 1:
        return 1
    else:
        return a * func(a - 1)

print func(5)

myFunc = lambda x : if x == 1:
return 1

myFunc(1)
