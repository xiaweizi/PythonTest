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

## 什么是迭代

在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）。

在Python中，迭代是通过 for ... in 来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：

	for (i=0; i<list.length; i++) {
	    n = list[i];
	}

可以看出，Python的for循环抽象程度要高于Java的for循环。

因为 Python 的 for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。

因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。

	注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
	1. 有序集合：list，tuple，str和unicode；
	2. 无序集合：set
	3. 无序集合并且具有 key-value 对：dict
	
而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。

迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。

## 索引迭代

Python中，迭代永远是取出元素本身，而非元素的索引。

对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？

方法是使用 enumerate() 函数：

	>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
	>>> for index, name in enumerate(L):
	...     print index, '-', name
	... 
	0 - Adam
	1 - Lisa
	2 - Bart
	3 - Paul

## 迭代 dict 的 value

我们已经了解了dict对象本身就是可迭代对象，用 for 循环直接迭代 dict，可以每次拿到dict的一个key。

如果我们希望迭代 dict 对象的value，应该怎么做？

dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：

	d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
	print d.values()
	# [85, 95, 59]
	for v in d.values():
	    print v
	# 85
	# 95
	# 59
	
如果仔细阅读Python的文档，还可以发现，dict除了values()方法外，还有一个 itervalues() 方法，用 itervalues() 方法替代 values() 方法，迭代效果完全一样：

	d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
	print d.itervalues()
	# <dictionary-valueiterator object at 0x106adbb50>
	for v in d.itervalues():
	    print v
	# 85
	# 95
	# 59
	
那这两个方法有何不同之处呢？

1. values() 方法实际上把一个 dict 转换成了包含 value 的list。

2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。

3. 打印 itervalues() 发现它返回一个 <dictionary-valueiterator> 对象，这说明在Python中，for 循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，任何可迭代对象都可以作用于for循环，而内部如何迭代我们通常并不用关心。

如果一个对象说自己可迭代，那我们就直接用 for 循环去迭代它，可见，迭代是一种抽象的数据操作，它不对迭代对象内部的数据有任何要求。

## 迭代 dict 的 key

我们了解了如何迭代 dict 的key和value，那么，在一个 for 循环中，能否同时迭代 key和value？答案是肯定的。

首先，我们看看 dict 对象的 items() 方法返回的值：

	>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
	>>> print d.items()
	[('Lisa', 85), ('Adam', 95), ('Bart', 59)]
	
## 生成列表

	>>> range(1, 11)
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
	>>> L = []
	>>> for x in range(1, 11):
	...    L.append(x * x)
	... 
	>>> L
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：

	>>> [x * x for x in range(1, 11)]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成 list。

写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

## 复杂表达式

使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。

假设有如下的dict：

	d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
	
	print([(x,y+1 )for x,y in d.items()])
	
## 条件过滤

列表生成式的 for 循环后面还可以加上 if 判断。例如：

	>>> [x * x for x in range(1, 11)]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
如果我们只想要偶数的平方，不改动 range()的情况下，可以加上 if 来筛选：

	>>> [x * x for x in range(1, 11) if x % 2 == 0]
	[4, 16, 36, 64, 100]
	
有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。	

## 高阶函数

**map**

`map`其实就是将一个`iterable`里的数据一次取出来，然后进行相应的函数操作，并顺序返回成`iterable`。

	>>> def f(x):
	...     return x * x
	...
	>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
	>>> list(r)
	[1, 4, 9, 16, 25, 36, 49, 64, 81]

**reduce**

`reduce`针对于`iterable`，依次取出两个数进行函数处理，返回的值再与下一个数进行函数处理，最后返回最终的结果。

	>>> def add(x, y):
	...     return x + y
	...
	>>> reduce(add, [1, 3, 5, 7, 9])
	25

**filter**

顾名思义，就是对集合进行刷选，针对传入函数的返回值进行判断，如果为`True`则保留，否则直接删除。

	def is_odd(n):
	    return n % 2 == 1
	
	list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
	
**sorted**

排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

Python内置的sorted()函数就可以对list进行排序：

	>>> sorted([36, 5, -12, 9, -21], key=abs)
	[5, 9, -12, -21, 36]
	

## 其他函数

**返回函数**

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：

	def calc_sum(*args):
	    ax = 0
	    for n in args:
	        ax = ax + n
	    return ax

但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：

	def lazy_sum(*args):
	    def sum():
	        ax = 0
	        for n in args:
	            ax = ax + n
	        return ax
	    return sum

当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：

	>>> f = lazy_sum(1, 3, 5, 7, 9)
	>>> f
	<function lazy_sum.<locals>.sum at 0x101c6ed90>

调用函数f时，才真正计算求和的结果：

	>>> f()
	25

**闭包**

注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：

	def count():
	    fs = []
	    for i in range(1, 4):
	        def f():
	             return i*i
	        fs.append(f)
	    return fs
	
	f1, f2, f3 = count()

在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：

	>>> f1()
	9
	>>> f2()
	9
	>>> f3()
	9

> 注： 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

	def count():
	    def f(j):
	        def g():
	            return j*j
	        return g
	    fs = []
	    for i in range(1, 4):
	        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
	    return fs

再看看结果：

	>>> f1, f2, f3 = count()
	>>> f1()
	1
	>>> f2()
	4
	>>> f3()
	9

**匿名函数**

当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
	
	>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
	[1, 4, 9, 16, 25, 36, 49, 64, 81]

**装饰器函数**

	def log(func):
	    def wrapper(*args, **kw):
	        print('call %s():' % func.__name__)
	        return func(*args, **kw)
	    return wrapper
	    
观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

	@log
	def now():
	    print('2015-3-25')
	    
调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：

	>>> now()
	call now():
	2015-3-25

把@log放到now()函数的定义处，相当于执行了语句：

	now = log(now)

由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

	def log(text):
	    def decorator(func):
	        def wrapper(*args, **kw):
	            print('%s %s():' % (text, func.__name__))
	            return func(*args, **kw)
	        return wrapper
	    return decorator
	    
这个3层嵌套的decorator用法如下：

	@log('execute')
	def now():
	    print('2015-3-25')
	    
和两层嵌套的decorator相比，3层嵌套的效果是这样的：

	>>> now = log('execute')(now)

因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

import functools

	def log(func):
	    @functools.wraps(func)
	    def wrapper(*args, **kw):
	        print('call %s():' % func.__name__)
	        return func(*args, **kw)
	    return wrapper
	    
或者针对带参数的decorator：

	import functools
	
	def log(text):
	    def decorator(func):
	        @functools.wraps(func)
	        def wrapper(*args, **kw):
	            print('%s %s():' % (text, func.__name__))
	            return func(*args, **kw)
	        return wrapper
	    return decorator
	    
**偏函数**

Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。

在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

	def int2(x, base=2):
	    return int(x, base)

这样，我们转换二进制就非常方便了：

	>>> int2('1000000')
	64
	>>> int2('1010101')
	85

## 类和实例

面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

仍以Student类为例，在Python中，定义类是通过class关键字：

	class Student(object):
	    pass

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

> 注：特殊方法`__init__`前后分别有两个下划线

注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

	>>> bart = Student('Bart Simpson', 59)
	>>> bart.name
	'Bart Simpson'
	>>> bart.score
	59
	
	class Student(object):
	    def __init__(self, name, score):
	        self.name = name
	        self.score = score
	
	    def get_grade(self):
	        if self.score >= 90:
	            return 'A'
	        elif self.score >= 60:
	            return 'B'
	        else:
	            return 'C'

## 访问限制

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

	class Student(object):
	
	    def __init__(self, name, score):
	        self.__name = name
	        self.__score = score
	
	    def print_score(self):
	        print('%s: %s' % (self.__name, self.__score))
	        
改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：

	>>> bart = Student('Bart Simpson', 59)
	>>> bart.__name
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'Student' object has no attribute '__name'
	
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

## 继承和多态

多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：

对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树.

## 获取对象信息

**使用 type()**

	>>> type(123)==type(456)
	True
	>>> type(123)==int
	True
	>>> type('abc')==type('123')
	True
	>>> type('abc')==str
	True
	>>> type('abc')==type(123)
	False
	
**使用 isinstance()**

	>>> isinstance('a', str)
	True
	>>> isinstance(123, int)
	True
	>>> isinstance(b'a', bytes)
	True
	
**使用 dir()**

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
	
	>>> dir('ABC')
	['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
	
## 实例属性和类属性

由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：

	class Student(object):
	    def __init__(self, name):
	        self.name = name
	
	s = Student('Bob')
	s.score = 90

但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

	class Student(object):
	    name = 'Student'
	    
当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：

	>>> class Student(object):
	...     name = 'Student'
	...
	>>> s = Student() # 创建实例s
	>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
	Student
	>>> print(Student.name) # 打印类的name属性
	Student
	>>> s.name = 'Michael' # 给实例绑定name属性
	>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
	Michael
	>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
	Student
	>>> del s.name # 如果删除实例的name属性
	>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
	Student
	
## 使用 __slots__

尝试给实例绑定一个属性:
	
	class Student(object):
	    pass
	>>> s = Student()
	>>> s.name = 'Michael' # 动态给实例绑定一个属性
	>>> print(s.name)
	Michael

为了给所有实例都绑定方法，可以给class绑定方法：

	>>> def set_score(self, score):
	...     self.score = score
	...
	>>> Student.set_score = set_score

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

	class Student(object):
	    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的.

## 使用 @property

	class Student(object):
	
	    def get_score(self):
	         return self._score
	
	    def set_score(self, value):
	        if not isinstance(value, int):
	            raise ValueError('score must be an integer!')
	        if value < 0 or value > 100:
	            raise ValueError('score must between 0 ~ 100!')
	        self._score = value
	
但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

	class Student(object):
	
	    @property
	    def score(self):
	        return self._score
	
	    @score.setter
	    def score(self, value):
	        if not isinstance(value, int):
	            raise ValueError('score must be an integer!')
	        if value < 0 or value > 100:
	            raise ValueError('score must between 0 ~ 100!')
	        self._score = value
 
 @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作。