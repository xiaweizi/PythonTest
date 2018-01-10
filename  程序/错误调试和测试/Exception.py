try:
    print 'try..'
    result = 10 / 0
    print result
except BaseException as e:
    print 'e:', e
else:
    print 'else'
finally:
    print 'finally'
print 'END'

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

class MyException(ValueError):
    pass
def test(x):
    if x == 0:
        raise MyException('invalid values: %s' % x)
    return x

# print test(0)

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
