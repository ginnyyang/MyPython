#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#__slots__我们已经知道怎么用了，参见slots.py ,__len__()方法我们也知道是为了能让class作用于len()函数。
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__getattr__
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
#要避免这个错误，除了可以加上一个属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
class Student(object):
	def __init__(self):
		self.name='yangjing'

	def __getattr__(self,attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda:25#返回函数也可以，但注意调用方式
s=Student()
#只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
print(s.name)
print(s.score)
print(s.age())
#任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None
print(s.male)