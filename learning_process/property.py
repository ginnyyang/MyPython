#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数

class Student(object):
	
	def get_score(self):
		return self._score
		
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value <0 or value>100:
			raise ValueError('score must be 0~100')
		self._score=value
		
#现在，对任意的Student实例进行操作，就不能随心所欲地设置score了
s=Student()
s.set_score(60)
print(s.get_score())
#s.set_score('asd')#ValueError: score must be an integer
#s.set_score(999)#ValueError: score must be 0~100