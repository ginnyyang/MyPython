#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#如果一个函数在内部调用自身本身，这个函数就是递归函数，典型的例子就是阶乘
#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
	
print(fact(1))
print(fact(5))
print(fact(100))

#使用递归函数需要注意防止栈溢出。
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
print(fact(1000))
