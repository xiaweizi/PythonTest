# -*- coding: utf-8 -*-
import types

class Animal(object):
    def run(self):
        print 'Animal is running....'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'
    def __len__(self):
        return 100

print type(Animal)

animal = Animal()
cat = Cat()
print type(animal)

a = 123
print type(a)

def test():
    pass

print type(test) == types.FunctionType

print isinstance(cat, (Animal))

print dir('abc')

print dir(animal)

print len(cat)

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x + self.x

obj = MyObject()

print hasattr(obj, '1x')
print obj.x
setattr(obj, 'x', 12)
print obj.x
setattr(obj, 'y', 'xia')
print hasattr(obj, 'y')
print obj.y

print getattr(obj, 'z', 'None')
