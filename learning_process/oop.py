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
#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
#特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名

#有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
#但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
#但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名
print(yangjing._Student__name)

#最后注意下面的这种错误写法
yangjing.__name='New name'
#表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
#内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
print(yangjing.__name)
print(yangjing.get_name())


