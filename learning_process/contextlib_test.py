#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

from contextlib import contextmanager

class Query(object):

	def __init__(self,name):
		self.name=name
		
	def query(self):
		print('Query info about %s...'%self.name)

@contextmanager
def create_query(name):
	print('Begin')
	q=Query(name)
	yield q
	print('End')
	
with create_query('Bob') as q:
	q.query()
	
#很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
#代码的执行顺序是：
#with语句首先执行yield之前的语句，因此打印出<h1>；
#yield调用会执行with语句内部的所有语句，因此打印出hello和world；
#最后执行yield之后的语句，打印出</h1>
@contextmanager
def tag(name):
	print("<%s>"%name)
	yield
	print("</%s>"%name)
	
with tag("h1"):
	print("hello")
	print("world")
	
#如果一个对象没有实现上下文，我们就不能把它用于with语句。
#这个时候，可以用closing()来把该对象变为上下文对象。
from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.python.org')) as page:
	for line in page:
		print(line)

