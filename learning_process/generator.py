#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#受到内存限制，列表容量肯定是有限的。
#创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#第一种方法很简单，只要把一个列表生成式的[]改成()
g=(x*x for x in range(10))
#使用for循环打印g的元素
for n in g:
	print(n)
	
#如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
		a,b=b,a+b
		n=n+1
	return 'Done'
	
for m in fib(6):
	print(m)
#发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
h=fib(6)
while True:
	try:
		x=next(h)
		print('h:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break

