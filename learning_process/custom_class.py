#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#__slots__我们已经知道怎么用了，参见slots.py ,__len__()方法我们也知道是为了能让class作用于len()函数。
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__call__
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
	def __init__(self,name):
		self.name=name
		
	def __call__(self):
		print('My name is %s'%(self.name))
		
s=Student('yangjing')
s()

#那么，怎么判断一个变量是对象还是函数呢？
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(Student))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))