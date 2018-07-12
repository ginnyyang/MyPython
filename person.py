#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])
#上面复杂的调用可以简化
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数**kw
person('Jack',24,**extra)