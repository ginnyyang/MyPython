#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。

class Student(object):
	pass
	
#创建一个实例
s=Student()
#实例绑定一个属性
s.name='yangjing'
print(s.name)


#实例绑定一个方法
def set_age(self,age):
	self.age=age
	
from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

#但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2=Student()
#s2.set_age(30)
#print(s2.age)#AttributeError: 'Student' object has no attribute 'set_age'

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
	self.score=score
	
Student.set_score=set_score
s.set_score(90)
s2.set_score(100)
print(s.score)
print(s2.score)