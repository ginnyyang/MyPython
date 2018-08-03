#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

#错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理
#如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
try:
	print('try...')
	r=10/int('a')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('except:',e)
else:
	print('no error')
finally:
	print('finally...')
print('END')

