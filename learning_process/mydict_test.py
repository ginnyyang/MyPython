#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):#编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
	#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
	#对每一类测试都需要编写一个test_xxx()方法。
	#由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。
	#最常用的断言就是assertEqual()
	
	#可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
	#setUp()和tearDown()方法有什么用呢？
	#设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
		
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key,'value')
		
	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
		
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']
			
	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value=d.empty
			
	def setUp(self):
		print('setUp......')
		
	def tearDown(self):
		print('tearDown......')
		
#在命令行通过参数-m unittest直接运行单元测试
#python -m unittest mydict_test.py
#.....
#----------------------------------------------------------------------
#Ran 5 tests in 0.002s
#
#OK



#python -m unittest mydict_test.py
#setUp......
#tearDown......
#.setUp......
#tearDown......
#.setUp......
#tearDown......
#.setUp......
#tearDown......
#.setUp......
#tearDown......
#.
#----------------------------------------------------------------------
#Ran 5 tests in 0.000s
#
#OK



#对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
#class Student(object):
#    def __init__(self, name, score):
#        self.name = name
#        self.score = score
#    def get_grade(self):
#        if self.score >= 60:
#            return 'B'
#        if self.score >= 80:
#            return 'A'
#        return 'C'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score <0 or self.score>100:
            raise ValueError('score must be in 0 to 100')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

