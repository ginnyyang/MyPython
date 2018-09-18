#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
#绝大多数情况下，我们只需要使用threading这个高级模块。
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
#import time,threading
#
#def loop():
#	print('thread %s is running...'%threading.current_thread().name)
#	n=0
#	while n<5:
#		n=n+1
#		print('thread %s >>>%s'%(threading.current_thread().name,n))
#		time.sleep(1)
#	print('thread %s ended.'%threading.current_thread().name)
#
#print('thread %s is running...'%threading.current_thread().name)
#t=threading.Thread(target=loop,name='LoopThread')
#t.start()
#t.join()
#print('thread %s ended.'%threading.current_thread().name)

#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
#而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
#因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
#balance = balance + n
#也分两步：
#计算balance + n，存入临时变量中；
#将临时变量的值赋给balance。
#也就是可以看成：
#x = balance + n
#balance = x
#而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了
#import time,threading
#
#balance=0
#
#def change_it(n):
#	global balance
#	balance=balance+n
#	balance=balance-n
#	
#def run_thread(n):
#	for i in range(100000):
#		change_it(n)
#		
#t1=threading.Thread(target=run_thread,args=(5,))
#t2=threading.Thread(target=run_thread,args=(8,))
#t1.start()
#t2.start()
#t1.join()
#t2.join()
#print(balance)

#要确保balance计算正确，就要给change_it()上一把锁，
#当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
#由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
import time,threading

balance=0
lock=threading.Lock()

def change_it(n):
	global balance
	balance=balance+n
	balance=balance-n
	
def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()#获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)