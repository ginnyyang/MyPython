#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
#对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
#birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来

class Student(object):
	
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self,value):
		self._birth=value
		
	@property
	def age(self):
		return 2018-self.birth
#现在，对任意的Student实例进行操作，就不能随心所欲地设置score了
s=Student()
s.birth=1983
print(s.age)

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('width must be an integer')
		if value < 0:
			raise ValueError('width must be >0')
		self._width=value
		
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('height must be an integer')
		if value < 0:
			raise ValueError('height must be >0')
		self._height=value
		
	@property
	def resolution(self):
		return self._width * self._height
		
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
	print('测试通过!')
else:
	print('测试失败!')