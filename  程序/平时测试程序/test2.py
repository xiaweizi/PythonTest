class Student(object):
    def run():
        print 'Student...'

class Person(Student):
    def run():
        print 'Person...'

def sum(x):
    return x + x

s = sum

print isinstance(s, sum)
