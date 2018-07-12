#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。

#命名关键字参数可以有缺省值，从而简化调用
def person(name,age,*,city='Beijing',job):
	print(name,age,city,job)

person('Jack',24,job='Engineer')
