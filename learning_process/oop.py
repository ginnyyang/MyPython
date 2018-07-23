#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
class Student(object):

	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender
		
	def get_gender(self):
		return self.__gender
		
	def set_gender(self,gender):
		if (gender=='male' or gender=='female'):
			self.__gender=gender
		else:
			raise ValueError('bad gender')

yangjing=Student('Ginny Yang','male')
print(yangjing.get_gender())
yangjing.set_gender('female')
print(yangjing.get_gender())
yangjing.set_gender('x')



