#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('begin call------')
        before = time.time()
        r=fn(*args, **kwargs)
        consumed=(time.time()-before)*1000
        print('%s executed in %s ms' % (fn.__name__, consumed))
        print('end call-----------')
        return r
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x + y
print(fast(11,22))




