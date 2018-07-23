#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
#在Python中，一个.py文件就称之为一个模块（Module）。
#最大的好处是大大提高了代码的可维护性。
#其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
#我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。
#使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
#但是也要注意，尽量不要与内置函数名字冲突

#你也许还想到，如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
'a test module'#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__='Ginny Yang'#把作者写进去

import sys

#sys模块有一个argv变量，用list存储了命令行的所有参数。
#argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
#运行python3 hello.py获得的sys.argv就是['hello.py']；
#运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
def test():
	args=sys.argv
	if len(args)==1:
		print('Hello,world!')
	elif len(args)==2:
		print('Hello,%s!'%args[1])
	else:
		print('Too many arguments!')

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败，
#因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__=='__main__':
	test()
	
#在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
#在Python中，是通过_前缀来实现的

#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
#hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，那它们有什么用呢？
#我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
#这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
def _private_1(name):
	print('Hello,%s'%name)
	
def _private_2(name):
	print('Hi,%s'%name)
	
def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)

greeting('yangjing')
greeting('yj')
