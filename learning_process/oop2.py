#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
#新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）

#继承的第二个好处需要我们对代码做一点改进。
#你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal is running...，符合逻辑的做法是分别显示Dog is running...和Cat is running...，
#因此，对Dog和Cat类改进如下
class Animal(object):
	def run(self):
		print('Animal is running......')
		
class Dog(Animal):
	def run(self):
		print('Dog is running......')
		
class Cat(Animal):
	def run(self):
		print('Cat is running......')
		

dog=Dog()
dog.run()

cat=Cat()
cat.run()

#当子类和父类都存在相同的run()方法时,子类的run()覆盖了父类的run()，
#在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
#当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
a=list()
b=Animal()
c=Dog()
#判断一个变量是否是某个类型可以用isinstance()判断
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))#Dog是从Animal继承下来的，当创建了一个Dog的实例c时，c的数据类型是Dog，但c同时也是Animal

#要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
def run_twice(animal):
	animal.run()
	animal.run()
#传入Animal的实例就打印出：
#Animal is running...
#Animal is running...
run_twice(Animal())
#传入Dog的实例就打印出：
#Dog is running...
#Dog is running...
run_twice(Dog())

#看上去没啥意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从Animal派生
#新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly......')
	
run_twice(Tortoise())

#总结：多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
#因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
#由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
#而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
#这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
#这就是著名的“开闭”原则：
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数