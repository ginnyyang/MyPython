#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
import hashlib
def get_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

db = {
	'michael': 'e10adc3949ba59abbe56e057f20f883e',
	'bob': '878ef96e86145580c38c87f0410ad153',
	'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(username, password):
	user=db[username]
	if user == get_md5(password):
		return True
	else:
		return False
	
	
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

