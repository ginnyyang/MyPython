#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向对象的设计思想是抽象出Class，根据Class创建Instance

#在Python中，定义类是通过class关键字
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，
#紧接着是(object)，表示该类是从哪个类继承下来的,通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
	pass
	
#可以自由地给一个实例变量绑定属性
yangjing=Student()
yangjing.name='Ginny Yang'
print(yangjing.name)