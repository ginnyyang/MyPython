#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#采用多重继承。首先，主要的类层次按照哺乳类和鸟类设计

class Aniaml(object):
	pass

#哺乳类
class Mammal(Aniaml):
	pass
#鸟类
class Bird(Aniaml):
	pass
	
#给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
#class Runnable(object):
class RunnableMixin(object):
	def run(self):
		print('running......')
		
#class Flyable(object):
class FlyableMixin(object):
	def fly(self):
		print('flying......')
		
class CarnivorousMixIn(object):
	def Carnivorous(self):
		print('eat meat......')
		
class HerbivoresMixIn(object):
	def Herbivores(self):
		print('not eat meat......')

#各种动物
class Dog(Mammal,Runnable):
	pass

class Bat(Mammal,Flyable):
	pass
	
class Parrot(Bird,Flyable):
	pass

#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
#但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
#为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn
#还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：
#class Ostrich(Bird,Runnable):
class Ostrich(Bird,RunnableMixin,HerbivoresMixIn):
	pass
	
#Python自带的很多库也使用了MixIn。
#举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。
#通过组合，我们就可以创造出合适的服务来
	
#编写一个多进程模式的TCP服务，定义如下：
class myTCPServer(TCPServer,ForkingMinIn):
	pass
	
#编写一个多线程模式的UDP服务，定义如下：
class myTCPServer(TCPServer,ThreadingMixIn):
	pass
	
#编写一个CoroutineMixIn：
class myTCPServer(TCPServer,CoroutineMixIn):
	pass

