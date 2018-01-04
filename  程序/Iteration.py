for value in range(1, 100):
	if value % 7 == 0:
		print(value)

L = ['a', 'b', 'c', 'd']
for index,name in enumerate(L):
	print index, '-', name

B = {'a':1, 'b':2, 'c':3}

for value in B.itervalues():
	print(value)

C = B.items()
C.append(1)
print(C)

E= [(1,2),2,3,4]
E.append(5)
print(E)