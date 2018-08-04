#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
s='0'
n=int(s)
print(10/n)

#执行结果：
#python -m pdb debug.py------->启动
#> c:\users\jingoal\mypython\learning_process\debug.py(5)<module>()
#-> s='0'--------------------->pdb定位到下一步要执行的代码-> s = '0'
#(Pdb) l---------------------->输入命令l来查看代码
#  1     #!/usr/bin/env python3
#  2     # -*- coding: utf-8 -*-
#  3
#  4     #第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
#  5  -> s='0'
#  6     n=int(s)
#  7     print(10/n)
#  8
#  9     #执行结果：
# 10
# 11
#(Pdb) n------------------------>输入命令n可以单步执行代码
#> c:\users\jingoal\mypython\learning_process\debug.py(6)<module>()
#-> n=int(s)
#(Pdb) p s--------------------->任何时候都可以输入命令p 变量名来查看变量
#'0'
#(Pdb) n
#> c:\users\jingoal\mypython\learning_process\debug.py(7)<module>()
#-> print(10/n)
#(Pdb) p n
#0
#(Pdb) q---------------------->输入命令q结束调试，退出程序

#这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊


