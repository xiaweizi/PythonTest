def fun():
    global a
    a = 11
    a += 1
    print a
fun()
a += 1
print a

c  = 10
def test():
    c = 2
    print c

test()
