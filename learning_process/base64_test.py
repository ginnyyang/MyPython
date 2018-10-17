#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#写一个能处理去掉=的base64解码函数
import base64

def safe_base64_decode(s):
	num = len(s)%4
	s = s+b"="*num
	return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')