#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

#如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
#既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
#Python内置的logging模块可以非常容易地记录错误信息
import logging
def foo(s):
	return 10/int(s)
	
def bar(s):
	return foo(s)*2
	
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()
print('END')
#执行结果：同样是出错，但程序打印完错误信息后会继续执行，并正常退出
#ERROR:root:division by zero
#Traceback (most recent call last):
#  File "err_logging.py", line 13, in main
#    bar('0')
#  File "err_logging.py", line 9, in bar
#    return foo(s) * 2
#  File "err_logging.py", line 6, in foo
#    return 10 / int(s)
#ZeroDivisionError: division by zero
#END