#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

#dict迭代key
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
d={'a':1,'b':2,'c':3}
for key in d:
	print(key)
print('--------------------------------')
#dict迭代value
for value in d.values():
	print(value)
print('--------------------------------')
#dict迭代key,value
for k,v in d.items():
	print(k,v)
print('--------------------------------')


#迭代字符串
for ch in 'ABC':
	print(ch)
print('--------------------------------')
	
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
print('--------------------------------')

#如果要对list实现类似Java那样的下标循环怎么办？
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
	print(i,value)
	
for x,y in [(1,1),(2,4),(3,9)]:
	print(x,y)