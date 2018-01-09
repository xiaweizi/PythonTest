# -*- coding: utf-8 -*-

datas = {'a', 'b', 'c', 'd'}
for data in datas:
	print(data)

nums = {1,2,3,4,5}
sum = 0
for num in nums:
	sum += num
print(sum)

print(range(10))
print(list(range(10)))

## 算出 1 到 100 的和
sum = 0
for num in range(101):
	sum += num
print(sum)

# While
sum = 0
n = 0
while n <= 100:
	sum += n
	n += 1
print(sum)

# 1 - 10 找出第一个偶数
n = 1
while n <= 10:
	n += 1
	if n % 2 == 0:
		print(n)
		continue
