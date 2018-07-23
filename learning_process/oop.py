#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
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
		
#	def get_grade(self):
#		if self.score>90:
#			return 'A'
#		elif self.score>=60:
#			return 'B'
#		else:
#			return 'C'
	
yangjing=Student('Ginny Yang',100)
print(yangjing.get_name(),':',yangjing.get_score())

