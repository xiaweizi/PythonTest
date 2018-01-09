#1 /usr/bin/env python3
# -*- coding: utf-8 -*-

datas = ['a', 'b', 'c', 'd']
print(datas)

print(len(datas))

print(datas[1])
print(datas[-1])
print(datas[-2])

datas.append('e')
print(datas)

datas.insert(1, 'a')
print(datas)

datas.pop()
print(datas)

datas.pop(1)
print(datas)

datas1 = [1, 2, 3]
datas.append(datas1)
print(datas)

print(len(datas))
print(datas[-1][0])
print(datas[0][0])

datas == ()
print(datas)


tuble = ('a', 'b', 'c', 'd')
print(tuble[1])

tuble = ()
print(tuble)

tuble = (1)
print(tuble)

tuble = (1,)
print(tuble)