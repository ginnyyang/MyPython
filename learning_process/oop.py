#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，
#所以，我们把Student类改一改：
class Student(object):

	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	
	def print_score(self):
		print('%s:%s'%(self.__name,self.__score))
		
#	def get_grade(self):
#		if self.score>90:
#			return 'A'
#		elif self.score>=60:
#			return 'B'
#		else:
#			return 'C'
	
yangjing=Student('Ginny Yang',100)
print(yangjing.__name)
