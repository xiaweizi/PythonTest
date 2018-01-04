## 赘述

`mac`自带`python2.7`版本，但是最新版本和旧版本不兼容，所以还是决定重新下载新版本，并且新版本是可以和旧版本兼容的。

在安装的时候还是会遇到一些小坑，特此记录一些命令行的使用，方便后期查找。

	sudo vim ~/.bash_profile //修改本地的环境变量
	echo $PATH // 查看本地的环境变量
	source ~/.bash_profile // 让刚刚设置的环境变量生效

使用中文添加的配置

	# -*- coding: utf-8 -*-
	
## 数据类型

**整数**

Python可以处理任意大小的整数，当然包括负整数，在Python程序中，整数的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。

计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

**浮点数**

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

**字符串**

字符串是以''或""括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。

如果需要用掉`''`或者`""`这个时候外层嵌套就需要对应相反的符号

如果同时包含的话，就需要转义字符：

	'Bob said \"I\'m OK\".'
	\n 表示换行
	\t 表示一个制表符
	\\ 表示 \ 字符本身

如果里面又用到了反斜杠那么就需要`raw`字符

	r'\(~_~)/ \(~_~)/'

如果需要表示多行的话

	'''Line 1
	Line 2
	Line 3'''

**布尔值**

布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来。

布尔值可以用and、or和not运算。

and运算是与运算，只有所有都为 True，and运算结果才是 True。

or运算是或运算，只要其中有一个为 True，or 运算结果就是 True。

not运算是非运算，它是一个单目运算符，把 True 变成 False，False 变成 True。

**空值**

空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

## list

`Python`内置的一种数据类型是列表，`list`是一种**有序**的集合，可以随时添加和删除其中的元素.`list`是数学意义上的有序集合，也就是说，`list`中的元素是按照顺序排列的。

命名方式

L = ['Michael', 100, True]
empty_list = []

**查询** `L[1]`、`L[-1]`

**添加** `L.append('da')`、`L.insert(0, '22')`

**删除** `L.pop()`、`L.pop(1)`

**修改** `L[0] = 'da'`

## tuple

`tuple`是另一种**有序**的列表，中文翻译为`元组`。`tuple`和`list`非常类似，但是`tuple`一旦创建完成，就不能再修改。

命名方式

t = ('Adam', 'Lisa', 'Bart')

用法同上，不过只能查询

因为创建单数据会有歧义，所以需要加个`，`

	t = (1,)
	t = ('Adam',)
	
## 逻辑语句

**if elif else**

计算机之所以能做很多自动化的任务，因为它可以自己做条件的判断。

> 注： Python 代码的缩进规则。具有相同缩进的代码被视为代码块。
> if 语句后接表达式，然后用 : 表示代码开始

	score = 85
	
	if score>=90:
	    print 'excellent'
	elif score>=80:
	    print 'good'
	elif score>=60:
	    print 'passed'
	else:
	    print 'failed'

**for**

	L = [75, 92, 59, 68]
	sum = 0.0
	for value in L:
	    sum += value
	print sum / 4
	
**while**

计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。

	sum = 0
	x = 1
	n = 1
	while True:
	    sum += x
	    x *= 2
	    n += 1
	    if n >20:
	        break
	print sum

0-100 只计算奇数的值

	sum = 0
	x = 0
	while True:
	    x = x + 1
	    if x > 100:
	        break
	    if x % 2 == 0:
	        continue
	    sum += x
	print sum

**多重循环**

1-100 十位数比各位数小的数

	for x in [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]:
	    for y in [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]:
	        if x < y:
	            print x * 10 + y

## dict

从字名可以理解为「字典」，类似于`java`中的`map`，是以键值对的方式存储。

dict的第一个特点是**查找速度快**，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。

不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。

由于dict是按 key 查找，所以，在一个dict中，**key不能重复**。

dict的第二个特点就是存储的key-value序对是**没有顺序**的！这和list不一样：

dict的第三个特点是作为 key 的元素必须**不可变**，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。

命名方式

	d = {
	    'Adam': 95,
	    'Lisa': 85,
	    'Bart': 59
	}
	
**查询** `d['Adam']`、`d.get('Adam')`,在取值的时候最好需要判断一下: 'Adam' in d.

**修改** `d['Adam'] = 32`

**增加** `d['Weizi'] = 32`

**删除** `d.pop('Adam')`、`del(d['Adam'])`

## set

dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。

有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。

set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。

set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。

set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

命名方式：

	s = set(['A', 'B', 'C'])

**查询** 由于set存储的是无序集合，所以我们没法通过索引来访问。访问 set中的某个元素实际上就是判断一个元素是否在set中。`'Bart' in s`。

**增加** `s.add(1)`

**删除** `s.remove(1)`

## 函数

函数用于解决重复的代码块，统一封装成一个功能，以便需要直接调用。

**调用 abs 函数**：

	>>> abs(100)
	100
	>>> abs(-20)
	20
	>>> abs(12.34)
	12.34
	
调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你

如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型

而比较函数 cmp(x, y) 就需要两个参数，如果 x<y，返回 -1，如果 x==y，返回 0，如果 x>y，返回 1：

	>>> cmp(1, 2)
	-1
	>>> cmp(2, 1)
	1
	>>> cmp(3, 3)
	0

**编写函数**

在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。

我们以自定义一个求绝对值的 my_abs 函数为例：

	def my_abs(x):
	    if x >= 0:
	        return x
	    else:
	        return -x
	        
**具有多返回值的函数**

函数也是可以拥有多个返回值的，比如我们经常遇到需要从一个点移动到另一点，给出坐标、位移和角度，就可以计算出新的坐标。

	import math
	def move(x, y, step, angle):
	    nx = x + step * math.cos(angle)
	    ny = y - step * math.sin(angle)
	    return nx, ny
	    
	>>> x, y = move(100, 100, 60, math.pi / 6)
	>>> print x, y
	151.961524227 70.0
	
其实返回的值是一个`tuple`

但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

**递归函数**

在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

	def fact(n):
	    if n==1:
	        return 1
	    return n * fact(n - 1)
	    
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试计算 fact(10000)。

**默认参数**

定义函数的时候，还可以有默认参数。

**函数的默认参数的作用是简化调用**，你只需要把必须的参数传进去，但是在需要的时候，又可以传入额外的参数来覆盖默认参数值。

我们来定义一个计算 x 的 N 次方的函数

	def power(x, n):
	    s = 1
	    while n > 0:
	        n = n - 1
	        s = s * x
	    return s
	    
**可变参数**

如果想一个函数能接收任意个参数，我们可以定义一个可变参数：

	def fn(*args):
	    print args

计算传入数的平均值：

	def average(*args):
	    sum = 0
	    if len(args) == 0:
	        return 0.0
	    for value in args:
	        sum += value
	    return sum * 1.0 / len(args)
	
	print average()
	print average(1, 2)
	print average(1, 2, 2, 3, 4)
	
可变参数也不是很神秘，Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。

## 对 list 进行切片

取一个list的部分元素是非常常见的操作。比如，一个list如下：

	>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']

	L = [1,2,3,4,5,6,7,8,9,10]
	print(L[0:4])
	print(L[1:3])
	print(L[:3])
	print(L[3:])
	print(L[::])
	print(L[0:4:2])
	print(L[2::3])
	print(L[2::3])
	
	[1, 2, 3, 4]
	[2, 3]
	[1, 2, 3]
	[4, 5, 6, 7, 8, 9, 10]
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	[1, 3]
	[3, 6, 9]

请利用切片，取出：

1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。

		L = range(1, 101)
		
		print L[0:10]
		print L[2::3]
		print L[4:50:5]

## 倒序切片

利用倒序切片对 1 - 100 的数列取出：

* 最后10个数；

* 最后10个5的倍数。

		L = range(1, 101)
		print L[-10:]
		print L[-46::5]
		
## 字符串切片

字符串有个方法 upper() 可以把字符变成大写字母：

	>>> 'abc'.upper()
	'ABC'
	
但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。

	def firstCharUpper(s):
	    return s[:1].upper()+s[1:]
	
	print firstCharUpper('hello')
	print firstCharUpper('sunday')
	print firstCharUpper('september')