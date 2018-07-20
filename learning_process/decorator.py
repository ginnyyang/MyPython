#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
	def decorator(func):
		def wrapper(*agrs,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*agrs,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2018-07-20')
now()

#我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
#再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
#以上两种decorator的定义都没有问题，但还差最后一步。
#因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
print(now.__name__)


