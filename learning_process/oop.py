#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
class Student(object):

	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	
	def print_score(self):
		print('%s:%s'%(self.__name,self.__score))
		
	def get_name(self):
		return self.__name
		
	def get_score(self):
		return self.__score
		
	def set_score(self,score):
		if 0<score<100:
			self.__score=score
		else:
			raise ValueError('bad score')
		
yangjing=Student('Ginny Yang',100)
print(yangjing.get_name(),':',yangjing.get_score())
yangjing.set_score(10)
print(yangjing.get_name(),':',yangjing.get_score())
yangjing.set_score(200)
print(yangjing.get_name(),':',yangjing.get_score())



