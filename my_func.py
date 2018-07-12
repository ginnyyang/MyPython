#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#def power(x):#x 就是一个位置参数
#	return x * x
#
#print(power(5))
#print(power(15))

#X的n次方如何实现呢
def power(x,n):#x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
	s=1
	while(n>0):
		s=s*x
		n=n-1
	return s
		
print(power(5,1))
print(power(5,2))
print(power(5,3))
print(power(5))
	

