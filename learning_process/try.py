#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕

#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
#from functools import reduce
#
#def str2num(s):
#    return int(s)
#
#def calc(exp):
#    ss = exp.split('+')
#    ns = map(str2num, ss)
#    return reduce(lambda acc, x: acc + x, ns)
#
#def main():
#    r = calc('100 + 200 + 345')
#    print('100 + 200 + 345 =', r)
#    r = calc('99 + 88 + 7.6')
#    print('99 + 88 + 7.6 =', r)
#
#main()

from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()




