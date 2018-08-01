#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#__slots__我们已经知道怎么用了，参见slots.py ,__len__()方法我们也知道是为了能让class作用于len()函数。
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
#以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
		
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100000:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素
Fib()[5]#TypeError: 'Fib' object does not support indexing