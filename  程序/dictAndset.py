datas = {'a' : 1, 'b' : 2, 1 : '3'}
for data in datas:
	print(data)
	print(datas[data])

print(datas['a'])
print(datas.get('3', -1))

print('a' in datas)
print('c' in datas)

# delete
datas.pop('a')
print(datas)

print('--------------')
print(datas.keys())

c = datas.setdefault('a', 1)
print(c)
d = datas.setdefault('a', 2)
print(d)
print(datas)

print('set--------------')
sets = {1,2,3,4}

print(sets)