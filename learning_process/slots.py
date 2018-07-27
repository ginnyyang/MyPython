#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
#如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
	__slots__=('name','age')
	

s=Student()
s.name='yangjing'
print(s.name)
s.age=25
print(s.age)
#s.score=99
#print(s.score)#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
	pass

g=GraduateStudent()
g.score=100
print(g.score)

#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
