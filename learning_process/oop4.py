#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#实例属性属于各个实例所有，互不干扰；
#类属性属于类所有，所有实例共享一个属性；
#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误

class Student(object):
	name='Student'

#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
s=Student()
print(s.name)
print(Student.name)
s.name='yangjing'
print(s.name)
print(Student.name)
del s.name#在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
print(s.name)
print(Student.name)

#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student2(object):
	count=0
	
	def __init__(self,name):
		self.name=name
		Student2.count+=1
		
print('Students:', Student2.count)
bart = Student2('Bart')
print('Students:', Student2.count)
lisa = Student2('Lisa')
print('Students:', Student2.count)
print('测试通过!')

