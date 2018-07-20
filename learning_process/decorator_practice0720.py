#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import functools
import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        before = time.time()
        r=fn(*args, **kwargs)
        consumed=(time.time()-before)*1000
        print('%s executed in %s ms' % (fn.__name__, consumed))
        return r
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x + y
print(fast(11,22))



