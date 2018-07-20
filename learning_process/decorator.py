#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数对象有一个__name__属性，可以拿到函数的名字
def now():
	print('2018-07-19')
f=now
print(f.__name__)
print(now.__name__)



