#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#如果已经有一个list或tuple，要调用一个可变参数怎么办？
def calc(*numbers):#*代表可变参数
	sum=0
	for n in numbers:
		sum = sum + n * n 
	return sum

nums=[1,2,3]
#方法一,问题是太繁琐
print(calc(nums[0],nums[1],nums[2]))	
#方法二,*nums表示把nums这个list的所有元素作为可变参数传进去，这种写法最常见
print(calc(*nums))
