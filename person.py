#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name,age,*,city,job):
	print(name,age,city,job)

person('Jack',24,city='Beijing',job='Engineer')
