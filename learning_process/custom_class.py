#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#__slots__我们已经知道怎么用了，参见slots.py ,__len__()方法我们也知道是为了能让class作用于len()函数。
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__getitem__
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a

f=Fib()
print(f[0])
print(f[100])

