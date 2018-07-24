#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用type()函数,判断对象类型
#基本类型都可以用type()判断
print(type(123))
print(type('str'))
print(type(None))

#如果一个变量指向函数或者类，也可以用type()判断
print(type(abs))

class Animal(object):
	pass
a=Animal()
print(type(a))

#type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123)==type(456))
print(type(123)==int)
print(type('123')==type('abc'))
print(type('abc')==str)
print(type(123)==type('abc'))

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
	pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
#如果继承关系是：object -> Animal -> Dog -> Husky
print('-----object -> Animal -> Dog -> Husky---')
class Dog(Animal):
	pass

class Husky(Dog):
	pass
	
d=Dog()
h=Husky()

print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))
print(isinstance(d,Husky))

#能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('abc',str))

#还可以判断一个变量是否是某些类型中的一种
print(isinstance([1,2,3],(list,tuple)))

#总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”


#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('ABC'))

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
	def __init__(self):
		self.x=9
	
	def power(self):
		return self.x * self.x

obj=MyObject()
print(hasattr(obj,'x'))#有属性x吗
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)
#可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj,'z',404))


#也可以获得对象的方法
print(hasattr(obj,'power'))
fn=getattr(obj,'power')
print(fn())