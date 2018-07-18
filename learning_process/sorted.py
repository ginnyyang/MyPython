#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#sorted()函数可以接收一个key函数来实现自定义的排序
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted([36,5,-12,9,-21],key=abs))

#忽略大小写，按照字母序排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))


#用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
def by_name(t):
	return t[0]
L2=sorted(L,key=by_name)
print(L2)
#按成绩从高到低排序
def by_score(t):
	return t[1]
L3=sorted(L,key=by_score,reverse=True)
print(L3)
