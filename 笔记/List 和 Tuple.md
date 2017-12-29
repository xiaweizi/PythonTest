## List

使用`[]`表示

	>>> classmates = ['Michael', 'Bob', 'Tracy']
	>>> classmates
	['Michael', 'Bob', 'Tracy']
	
通过下标获取值

	>>> classmates[0]
	'Michael'
	>>> classmates[1]
	'Bob'
	>>> classmates[2]
	'Tracy'
	>>> classmates[3]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: list index out of range
	
倒叙获取

	>>> classmates[-1]
	'Tracy'
	>>> classmates[-2]
	'Bob'


**添加**

	>>> classmates.append('Adam')
	>>> classmates
	['Michael', 'Bob', 'Tracy', 'Adam']
	
**插入**

	>>> classmates.insert(1, 'Jack')
	>>> classmates
	['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
	
**删除**

	>>> classmates.pop()
	'Adam'
	>>> classmates
	['Michael', 'Jack', 'Bob', 'Tracy']
	
	>>> classmates.pop(1)
	'Jack'
	>>> classmates
	['Michael', 'Bob', 'Tracy']
	
**修改**

	>>> classmates[1] = 'Sarah'
	>>> classmates
	['Michael', 'Sarah', 'Tracy']
	
类型也可以不一样

	>>> L = ['Apple', 123, True]
	
元素也可以是`list`

	>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
	>>> len(s)
	4

类似于二维数组的数据获取 `s[2][2]`

## tuple

和`list`相似，数据不能修改，用`()`表示

	>>> classmates = ('Michael', 'Bob', 'Tracy')

内部的`list`数据是可以修改的

	>>> t = ('a', 'b', ['A', 'B'])
	>>> t[2][0] = 'X'
	>>> t[2][1] = 'Y'
	>>> t
	('a', 'b', ['X', 'Y'])

