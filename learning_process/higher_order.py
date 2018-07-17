#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#高阶函数英文叫Higher-order function
#一个函数接收另一个函数作为参数，这种函数就称之为高阶函数

#将函数调用结果付给变量
print('将函数调用结果付给变量')
x=abs(-10)
print(x)

#将函数本身赋值给变量
print('将函数本身赋值给变量')
f=abs
print(f(-10))

#一个最简单的高阶函数
print('一个最简单的高阶函数')
def add(x,y,f):
	return f(x)+f(y)
	
print(add(5,-6,abs))
