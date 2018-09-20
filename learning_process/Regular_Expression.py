#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#用\d可以匹配一个数字，\w可以匹配一个字母或数字,\s可以匹配一个空格（也包括Tab等空白符）
#用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
#要做更精确地匹配，可以用[]表示范围
#用()表示的就是要提取的分组（Group）

#尝试写一个验证Email地址的正则表达式。
#版本一应该可以验证出类似的Email
import re

def is_valid_email(addr):
	if re.match(r'[\w+\.]*\w+@\w+\.\w+',addr):
		return True
	else:
		return False
	
print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.org'))
print(is_valid_email('bob#example.com'))
print(is_valid_email('mr-bob@example.com'))

#版本二可以提取出带名字的Email地址：
def name_of_email(addr):
	d = re.match(r'([<\w+\s?\w+>]*\s?[\w+\.]*\w+)@\w+\.\w+', addr).group(1)
	if '<' in d:
		return d.split('<')[1].split('>')[0]
	return d
print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.org'))