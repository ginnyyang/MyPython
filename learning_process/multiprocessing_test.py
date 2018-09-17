#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#multiprocessing模块就是跨平台版本的多进程模块。

#multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
#创建子进程时，只需要传入一个执行函数和函数的参数
#创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#from multiprocessing import Process
#import os
#
#def run_proc(name):
#	print('Run child process %s (%s)...' %(name,os.getpid()))
#	
#if __name__=='__main__':
#	print('Parent process %s.' %os.getpid())
#	p=Process(target=run_proc,args=('test',))
#	print('Child process will start.')
#	p.start()
#	p.join()
#	print('Child process end.')
	
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
#from multiprocessing import Pool
#import os,time,random
#
#def long_time_task(name):
#	print('Run task %s (%s)...'%(name,os.getpid()))
#	start=time.time()
#	time.sleep(random.random()*3)
#	end=time.time()
#	print('Task %s runs %0.2f seconds.'%(name,(end-start)))
#	
#if __name__=='__main__':
#	print('Parent process %s.'%os.getpid())
#	#执行结果会发现task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
#	#因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制
#	p=Pool(4)#改成5试试
#	for i in range(5):
#		p.apply_async(long_time_task,args=(i,))
#	print('Waiting for all subprocesses done...')
#	p.close()
#	p.join()#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#	print('All subprocesses done.')

#很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
#import subprocess

#print('$ nslookup www.python.org')
#r=subprocess.call(['nslookup','www.python.org'])
#print('Exit code:',r)

#如果子进程还需要输入，则可以通过communicate()方法输入：
#print('$ nslookup')
#p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
#print(output.decode('utf-8','ignore'))
#print('Exit code:',p.returncode)
#上面的代码相当于在命令行执行命令nslookup，然后手动输入：
#set q=mx
#python.org
#exit

from multiprocessing import Process,Queue
import os,time,random

def write(q):
	print('Process to write:%s'%os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read:%s'%os.getpid())
	while True:
		value=q.get(True)
		print('Get %s from queue.'%value)
		
if __name__=='__main__':
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()

