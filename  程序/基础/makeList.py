B = range(1, 11, 2)
print(B)

print([x*x for x in range(1, 11)])

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

print(d.items())

print([(x,y+1 )for x,y in d.items()])

D = [x * x for x in range(1, 11) if x % 2 != 0]
print(D)