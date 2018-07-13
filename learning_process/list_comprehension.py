#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L=list(range(1,11))
print(L)

#要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
L1=[x*x for x in range(1,11)]
print(L1)

#for循环后面还可以加上if判断
L2=[x*x for x in range(1,11) if x%2==0]
print(L2)

#可以使用两层循环，可以生成全排列
L3=[m+n for m in 'ABC' for n in 'XYZ']
print(L3)

#列出当前目录下的所有文件和目录名
import os
L4=[d for d in os.listdir('.')]
print(L4)

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
l={'x':'A','y':'B','z':'C'}
L5=[k+'='+v for k,v in l.items()]
print(L5)

#把一个list中所有的字符串变成小写
s=['Hello','World','IBM','Apple']
L6=[i.lower() for i in s]
print(L6)

#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
#使用内建的isinstance函数可以判断一个变量是不是字符串
L7 = ['Hello', 'World', 18, 'Apple', None]
L8 = [i.lower() for i in L7 if isinstance(i,str)]
print(L8)