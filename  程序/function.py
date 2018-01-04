# function with some return value
import math

def power(x, n=2):
	s = 1
	while n > 0:
		n -= 1
		s *= x
	return s
print('power', power(3))
print('power', power(3, 3))

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)
print(fact(4))

def move(x, y, step, angle):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

value = move(100, 100, 60, math.pi / 6)
x, y= value

print(x, y)


def my_abs(x):
	if x < 0:
		return -x
	else:
		return x

print('my_abs', my_abs(-1))

print(abs(-100))

# compare funciton
print(cmp(1, 2))
print(cmp(2, 1))
print(cmp(3, 3))

# convert function

print(int('123'))
print(int(123.62))

print(str(1))

L = [1,2,3,4]
L.append(4)
B = set([1,2,3,4,4])
B.add(62)
print(L)
print(B)

L=[]
x = 0
while x < 99:
	x += 1
	L.append(x*x)
print(sum(L))