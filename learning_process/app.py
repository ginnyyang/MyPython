#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#处理3个URL，分别是：
#GET /：首页，返回Home；
#GET /signin：登录页，显示登录表单；
#POST /signin：处理登录表单，显示登录结果。
#注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中

#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return '<h1>Home</h1>'
	
@app.route('/signin',methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
			  
@app.route('/signin',methods=['POST'])
def signin():
	# 需要从request对象读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello,admin!</h3>'
	return '<h3>Bad username or password.</h3>'
	
if __name__=='__main__':
	app.run()
	
#运行python app.py，Flask自带的Server在端口5000上监听
#打开浏览器，输入首页地址http://localhost:5000/   显示home
#浏览器地址栏输入http://localhost:5000/signin，会显示登录表单
#输入预设的用户名admin和口令password，登录成功
#输入其他错误的用户名和口令，登录失败