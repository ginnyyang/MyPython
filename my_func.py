#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x,n=2):#默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
	s=1
	while(n>0):
		s=s*x
		n=n-1
	return s
		
print(power(5,1))
print(power(5,3))
print(power(5))


	

