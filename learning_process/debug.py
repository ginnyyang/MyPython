#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第5种方式也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
import pdb

s='0'
n=int(s)
pdb.set_trace()
print(10/n)

#执行结果：
#运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
#python debug.py
#> c:\users\jingoal\mypython\learning_process\debug.py(10)<module>()
#-> print(10/n)
#(Pdb) p n
#0
#(Pdb) c
#Traceback (most recent call last):
#  File "debug.py", line 10, in <module>
#    print(10/n)
#ZeroDivisionError: division by zero

#这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

#如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：
#Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。
#PyCharm：http://www.jetbrains.com/pycharm/
#另外，Eclipse加上pydev插件也可以调试Python程序。
#写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。
#虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器


