# -*- coding: utf-8 -*-

#
class Animal(object):
    def run(self):
        print 'Animal is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

def test(animal):
    animal.run()

animal = Animal()
animal = Cat()
test(animal)

class People(object):
    def __run(self):
        print 'People is running...'

def test1(people):
    people._People__run()

people = People()
test1(people)
