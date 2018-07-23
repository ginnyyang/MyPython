#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
#这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
class Student(object):

	def __init__(self,name,score):
		self.name=name
		self.score=score
	
	def print_score(self):
		print('%s:%s'%(self.name,self.score))
	
yangjing=Student('Ginny Yang',100)
yangjing.print_score()