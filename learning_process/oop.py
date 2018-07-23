#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
class Student(object):

	def __init__(self,name,score):
		self.name=name
		self.score=score
	
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
yangjing=Student('Ginny Yang',100)
print(yangjing.name)
print(yangjing.score)

#面向对象编程的一个重要特点就是数据封装。
#在上面的Student类中，每个实例就拥有各自的name和score这些数据。
#我们可以通过函数来访问这些数据，比如打印一个学生的成绩：

def print_score(std):
	print('%s:%s'%(std.name,std.score))

print_score(yangjing)