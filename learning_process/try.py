#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def foo(s):
	return 10/int(s)
	
def bar(s):
	return foo(s)*2
	
def main():
	bar('0')

main()
#执行结果：
#Traceback (most recent call last):--------告诉我们这是错误的跟踪信息
#  File "err.py", line 11, in <module>-----调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行
#    main()
#  File "err.py", line 9, in main----------调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行
#    bar('0')
#  File "err.py", line 6, in bar-----------原因是return foo(s) * 2这个语句出错了，但这还不是最终原因
#    return foo(s) * 2
#  File "err.py", line 3, in foo-----------原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了ZeroDivisionError
#    return 10 / int(s)
#ZeroDivisionError: division by zero
