#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
def foo(s):
	n=int(s)
	print('>>>n=%d'%n)#用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
	return 10/n
	
def main():
	foo('0')
	
main()

#执行结果：
#>>>n=0
#Traceback (most recent call last):
#  File "debug.py", line 13, in <module>
#    main()
#  File "debug.py", line 11, in main
#    foo('0')
#  File "debug.py", line 8, in foo
#    return 10/n
#ZeroDivisionError: division by zero

#