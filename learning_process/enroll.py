#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#如果要继续传入年龄、城市等信息，我们可以把年龄和城市设为默认参数
def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
	
enroll('Sarah','F')
#只有与默认参数不符的学生才需要提供额外的信息
enroll('Bob','M',7)
enroll('Adam','M',city='Tianjin')