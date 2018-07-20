#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

#通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
print(int('12345'))

#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print(int('12345',base=8))
print(int('12345',16))

#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(x,base=2):
	return int(x,base)
print(int2('1000000'))

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools
int3=functools.partial(int,base=2)
print(int3('1010101'))

#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)#实际上会把10作为*args的一部分自动加到左边
print(max2(5, 6, 7))