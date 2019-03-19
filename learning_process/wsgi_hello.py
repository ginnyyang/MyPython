#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
#HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
#复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body='<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]
	
	
#先启动服务端wsgi_server.py
#http://localhost:8000/ 显示hello web
#http://localhost:8000/yangjing  显示hello，yangjing