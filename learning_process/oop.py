#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
class Student(object):

	def __init__(self,name,score):
		self.name=name
		self.score=score
	
	def print_score(self):
		print('%s:%s'%(self.name,self.score))
		
	def get_grade(self):
		if self.score>90:
			return 'A'
		elif self.score>=60:
			return 'B'
		else:
			return 'C'
	
yangjing=Student('Ginny Yang',100)
yangjing2=Student('Ginny2 Yang',80)
yangjing3=Student('Ginny3 Yang',59)

print(yangjing.name,yangjing.get_grade())
print(yangjing2.name,yangjing2.get_grade())
print(yangjing3.name,yangjing3.get_grade())

#从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性
yangjing.score=10
yangjing.print_score()
