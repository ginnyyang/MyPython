#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#如果经常阅读Python的官方文档，可以看到很多文档都有示例代码
#可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致
#既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？
#答案是肯定的

#Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
class Dict(dict):
	'''
	Simple dict but also support access as x.y style.
	
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a=1, b=2, c='3')
	>>> d2.c
	'3'
	>>> d2['empty']
	Traceback (most recent call last):
		...
	KeyError: 'empty'
	>>> d2.empty
	Traceback (most recent call last):
		...
	AttributeError: 'Dict' object has no attribute 'empty'
	'''
	def __init__(self,**kw):
		super().__init__(**kw)
		
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
			
	def __setattr__(self,key,value):
		self[key]=value
		
if __name__=='__main__':
	import doctest
	doctest.testmod() 
	
#python mydict2.py
#
#什么输出也没有。
#这说明我们编写的doctest运行都是正确的。如果程序有问题，比如把__getattr__()方法注释掉，再运行就会报错

#python mydict2.py
#**********************************************************************
#File "mydict2.py", line 15, in __main__.Dict
#Failed example:
#    d1.x
#Exception raised:
#    Traceback (most recent call last):
#      File "C:\Users\jingoal\AppData\Local\Programs\Python\Python36\lib\doctest.py", line 1330, in __run
#        compileflags, 1), test.globs)
#      File "<doctest __main__.Dict[2]>", line 1, in <module>
#        d1.x
#    AttributeError: 'Dict' object has no attribute 'x'
#**********************************************************************
#File "mydict2.py", line 21, in __main__.Dict
#Failed example:
#    d2.c
#Exception raised:
#    Traceback (most recent call last):
#      File "C:\Users\jingoal\AppData\Local\Programs\Python\Python36\lib\doctest.py", line 1330, in __run
#        compileflags, 1), test.globs)
#      File "<doctest __main__.Dict[6]>", line 1, in <module>
#        d2.c
#    AttributeError: 'Dict' object has no attribute 'c'
#**********************************************************************
#1 items had failures:
#   2 of   9 in __main__.Dict
#***Test Failed*** 2 failures.


#对函数fact(n)编写doctest并执行
#def fact(n):
#    '''
#    Calculate 1*2*...*n
#
#    >>> fact(1)
#    1
#    >>> fact(10)
#    ?
#    >>> fact(-1)
#    ?
#    '''
#    if n < 1:
#        raise ValueError()
#    if n == 1:
#        return 1
#    return n * fact(n - 1)

def fact(n):
	'''
	Calculate 1*2*...*n
	
	>>> fact(1)
	1
	>>> fact(10)
	3628800
	>>> fact(-1)
	Traceback (most recent call last):
		...
	ValueError
	'''
	if n<1:
		raise ValueError()
	if n==1:
		return 1
	return n*fact(n-1)

if __name__ == '__main__':
	import doctest
	doctest.testmod()