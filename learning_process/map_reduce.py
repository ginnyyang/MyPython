#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
	return x*x 
	
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

#所有数字转为字符串
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#序列求和
from functools import reduce
def add(x,y):
	return x+y
	
print(reduce(add,[1,3,5,7,9]))

#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
	return x*10+y 
print(reduce(fn,[1,3,5,7,9]))

#把str转换为int的函数
def char2num(s):
	digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return digits[s]
print(reduce(fn,map(char2num,'13579')))	

#整理成一个str2int的函数就是
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2int(s):
	def fn(x,y):
		return x*10+y 
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))
	
print(str2int('24680'))

#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
	return(name[0].upper()+name[1:].lower())
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)	

#编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
	return reduce(lambda x, y: x*y, list(L))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))	

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
	return reduce(lambda x,y:x*10+y ,map(lambda x: digits[x], s.replace('.','')))/(10**s.index('.'))
print('str2float(\'123.456\') =', str2float('123.456'))

	
		
