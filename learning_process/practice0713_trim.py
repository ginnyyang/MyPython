#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#去除字符串首尾空格

def trim(s):
	while s[:1]==' ':
		s=s[1:]
	while s[-1:]==' ':
		s=s[:-1]
	return s

print(trim('hello '))
print(trim(' hello'))
print(trim(' hello '))
print(trim(' hello world '))
print(trim(''))
print(trim('    '))