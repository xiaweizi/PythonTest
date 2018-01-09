#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name = 'xiaweizi', age = 12):
        self.name = name
        self.age = age

    def to_string(self):
        print('姓名:%s, 年龄:%d' % (self.name , self.age))



student = Student('aa', 0)
student.set_name('nihao', 11)
student.to_string()
print (student.name, student.age)
