# -*- coding: utf-8 -*-

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[1]

print(sorted(students, key=lambda t: t[1]))
