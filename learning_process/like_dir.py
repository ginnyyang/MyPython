#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

def listdir(path) :
    curPath = os.path.abspath(path)
    print(curPath)
    print('   createTime   ', 'size ', 'fileName')
    for fn in os.listdir(curPath):
        absfile = os.path.join(path, fn)
        fileinfo = os.stat(absfile)
        createTime = time.strftime("%Y-%m-%d %X", time.localtime(fileinfo.st_ctime))
        filesize = ''
        if os.path.isfile(absfile):
            filesize += str(os.path.getsize(absfile))
        print(createTime, filesize, fn)

def search(path, des):
    for fn in os.listdir(path):
        absfile = os.path.join(path, fn)
        if os.path.isfile(absfile):
            if fn.find(des) != -1:
                print(absfile)
        else:
            search(absfile, des)

listdir(r'C:\Users\jingoal\MyPython\learning_process')
search(r'.' , '.py')