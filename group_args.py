#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
	
def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
	
f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

#通过一个tuple或dict也可以调用上述函数
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

args2=(1,2,3)
kw2={'d':88,'x':'#'}
f2(*args2,**kw2)