#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持

import asyncio
import threading

@asyncio.coroutine
def hello():
	print('Hello world! (%s)' %threading.currentThread())
	# 异步调用asyncio.sleep(1):
	yield from asyncio.sleep(1)
	print('Hello again! (%s)' %threading.currentThread())
	
# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#@asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行
#把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。