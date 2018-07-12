#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#如果参数个数不固定，可以把参数作为一个list或tuple传进来
def calc(numbers):
	sum=0
	for n in numbers:
		sum = sum + n * n 
	return sum
	
print(calc([1,2,3]))
print(calc((1,3,5,7)))
#利用可变参数，调用函数的方式可简化，目前是报错的
print(calc(1,2,3))
print(calc(1,3,5,7))