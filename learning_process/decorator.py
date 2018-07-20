#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#本质上，decorator就是一个返回函数的高阶函数
#我们要定义一个能打印日志的decorator，可以定义如下
#def log(func):
#	def wrapper(*agrs,**kw):
#		print('call %s():'%func.__name__)
#		return func(*agrs,**kw)
#	return wrapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
#我们要借助Python的@语法，把decorator置于函数的定义处：
#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)
#由于log()是一个decorator，返回一个函数，
#所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，
#即在log()函数中返回的wrapper()函数。
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
#在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
#@log
#def now():
#	print('2018-07-19')
#now()

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


