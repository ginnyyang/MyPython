#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行

def consumer():
	r=''
	while True:
		n=yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' %n)
		r='200 OK'
		
def produce(c):
	c.send(None)
	n=0
	while n<5:
		n=n+1
		print('[PRODUCER] Producing %s...' %n)
		r=c.send(n)
		print('[PRODUCER] Consumer return: %s' %r)
	c.close()
	
c=consumer()
produce(c)

#consumer函数是一个generator，把一个consumer传入produce后：
#
#首先调用c.send(None)启动生成器；
#
#然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
#consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
#produce拿到consumer处理的结果，继续生产下一条消息；
#
#produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务