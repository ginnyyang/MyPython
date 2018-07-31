#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#__slots__我们已经知道怎么用了，参见slots.py ,__len__()方法我们也知道是为了能让class作用于len()函数。
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__str__
#只需要定义好__str__()方法，返回一个好看的字符串就可以了：
class Student(object):
	def __init__(self,name):
		self.name=name
		
	def __str__(self):
		return 'Student object (name:%s)'%self.name

print(Student('yangjing'))
#Student object (name:yangjing)
#这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
#但是细心一点会发现直接敲变量不用print，打印出来的实例还是不好看
#这个需要在交互模式下尝试
#>>> class Student(object):
#...     def __init__(self, name):
#...             self.name=name
#...     def __str__(self):
#...             return 'Student object (name:%s)'%self.name
#...
#>>> s=Student('yangjing')
#>>> s
#<__main__.Student object at 0x000001F0209B6278>

#这是因为直接显示变量调用的不是__str__()，而是__repr__()，
#两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
#也就是说，__repr__()是为调试服务的。
#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

#>>> class Student(object):
#...     def __init__(self,name):
#...             self.name=name
#...     def __str__(self):
#...             return 'Student object (name:%s)'%self.name
#...     __repr__ = __str__
#...
#>>> s=Student('yangjing')
#>>> s
#Student object (name:yangjing)
