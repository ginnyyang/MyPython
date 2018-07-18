#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#filter()接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

#例如，在一个list中，删掉偶数，只保留奇数
def is_odd(n):
	return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
	
print(list(filter(not_empty,['A','','B',None,'C','   '])))

#用filter求素数
#1.先构造一个从3开始的奇数序列
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n
#2.定义一个筛选函数
def _not_divisible(n):
	return lambda x:x%n>0
#3.定义一个生成器，不断返回下一个素数,这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列
def primes():
	yield 2
	it=_odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(_not_divisible(n),it)
#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件
for n in primes():
	if n<100:
		print(n)
	else:
		break
		
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
	return str(n)==str(n)[::-1]
l=list(filter(is_palindrome, range(1, 200)))
for i in l:
	print(i)
	

