#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#__slots__我们已经知道怎么用了，参见slots.py ,__len__()方法我们也知道是为了能让class作用于len()函数。
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__str__
#先定义一个Student类，打印一个实例：
class Student(object):
	def __init__(self,name):
		self.name=name

print(Student('yangjing'))
#打印出一堆<__main__.Student object at 0x000001C39D5D5F98>，不好看
