#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当我们需要定义常量时,更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import Enum,unique

@unique#@unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
	print(name, '=>', member)
	
#把Student的gender属性改造为枚举类型，可以避免使用字符串
@unique
class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
	def __init__(self, name, gender):
		self.name = name
		if isinstance(gender,Gender):
			self.gender = gender
		else:
			raise ValueError('wrong value')
		
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
	print('测试通过!')
else:
	print('测试失败!')