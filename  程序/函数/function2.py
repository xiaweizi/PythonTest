def func1():
    print 'dd'
    return None

def func():
    print 'make function'
    global func1
    def func1():
        print 'inner function'
func1()
func()
