#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
#新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）

#可以对子类增加一些方法：
class Animal(object):
	def run(self):
		print('Animal is running......')
		
class Dog(Animal):
	def run(self):
		print('Dog is running......')
		
	def eat(self):
		print('Eating meat......')
	
class Cat(Animal):
	pass

dog=Dog()
dog.run()
dog.eat()
