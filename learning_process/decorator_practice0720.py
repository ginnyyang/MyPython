#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#再思考一下能否写出一个@log的decorator，使它既支持：
#@log
#def f():
#    pass
#又支持：
#
#@log('execute')
#def f():
#    pass

import functools
import time

def log(text=''):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print('%s begin call %s'%(text,fn.__name__))
            before = time.time()
            r=fn(*args, **kwargs)
            consumed=(time.time()-before)*1000
            print('%s executed in %s ms' % (fn.__name__, consumed))
            print('%s end call %s'%(text,fn.__name__))
            return r
        return wrapper
    return metric

@log()
def fast(x,y):
    time.sleep(0.0012)
    return x + y
print(fast(11,22))

@log('execute')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z
print(slow(1,2,3))




