#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name,age,*args,city,job):
	print(name,age,args,city,job)

#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
#person('Jack',24,city='Beijing',job='Engineer')
person('Jack',24,'Beijing','Engineer')
