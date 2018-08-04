#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

#如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(ValueError):
	pass
	
def foo(s):
	n=int(s)
	if n==0:
		raise FooError('invalid value:%s'%s)
	return 10/n

#foo('0')

#执行结果：（只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型）
#Traceback (most recent call last):
#  File "try.py", line 17, in <module>
#    foo('0')
#  File "try.py", line 14, in foo
#    raise FooError('invalid value:%s'%s)
#__main__.FooError: invalid value:0

#我们来看另一种错误处理的方式
def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError')
		raise
	
bar()

#执行结果：
#ValueError
#Traceback (most recent call last):
#  File "try.py", line 35, in <module>
#    bar()
#  File "try.py", line 30, in bar
#    foo('0')
#  File "try.py", line 14, in foo
#    raise FooError('invalid value:%s'%s)
#__main__.FooError: invalid value:0

#在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了
#其实这种错误处理方式相当常见。捕获错误目的只是记录一下，便于后续追踪。
#但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理
#raise语句如果不带参数，就会把当前错误原样抛出


#此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
#try:
#    10 / 0
#except ZeroDivisionError:
#    raise ValueError('input error!')
#只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。


