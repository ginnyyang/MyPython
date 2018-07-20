#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
#def log(text):
#	def decorator(func):
#		def wrapper(*agrs,**kw):
#			print('%s %s():'%(text,func.__name__))
#			return func(*agrs,**kw)
#		return wrapper
#	return decorator
#@log('execute')
#def now():
#	print('2018-07-20')
#now()

#我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
#再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
#以上两种decorator的定义都没有问题，但还差最后一步。
#因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
#print(now.__name__)

#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下
##针对带参数的decorator
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*agrs,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*agrs,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2018-7-20')
now()
print(now.__name__)




