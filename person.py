#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('Michael',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')