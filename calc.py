#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#利用可变参数，调用函数的方式可简化
def calc(*numbers):#*代表可变参数
	sum=0
	for n in numbers:
		sum = sum + n * n 
	return sum
	
print(calc(1,2,3))
print(calc(1,3,5,7))
print(calc(1,2))
print(calc())