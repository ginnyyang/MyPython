#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
try:
	print('try...')
	r=10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')

#从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，
#except由于捕获到ZeroDivisionError，因此被执行。
#最后，finally语句被执行。然后，程序继续按照流程往下走