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

#要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
	def __getattr__(self,attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda:25#返回函数也可以，但注意调用方式
		raise AttributeError('\'Student\' object has no attribution \'%s\''%attr)
s=Student()
#只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
print(s.name)
print(s.score)
print(s.age())
#print(s.male)

#这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
#举个例子：
#现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#http://api.server/user/friends
#http://api.server/user/timeline/list
#如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
	def __init__(self,path=''):
		self._path=path
		
	def __getattr__(self,path):
		return Chain('%s/%s'%(self._path,path))
		
	def __str__(self):
		return self._path
		
	__repr__=__str__
	
print(Chain().status.user.timeline.list)#这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！