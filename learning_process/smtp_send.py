#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件

#首先，我们来构造一个最简单的纯文本邮件：
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

#编写了一个函数_format_addr()来格式化一个邮件地址。
#注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
	
#构造MIMEText对象时，
#第一个参数就是邮件正文，
#第二个参数是MIME的subtype，传入'plain'表示纯文本，
#最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

#通过SMTP发出去：
#输入Email地址和口令
#from_addr=input('Form:')
from_addr="my2011card@163.com"
password=input('Password:')
#输入收件人地址
#to_addr=input('To:')
to_addr="jingoaltest201202@163.com"
#输入SMTP服务器地址
#smtp_server=input('SMTP server:')
smtp_server="smtp.163.com"

#构造MIMEText对象时，
#第一个参数就是邮件正文，
#第二个参数是MIME的subtype，传入'plain'表示纯文本，
#最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
#msg=MIMEText('hello, send by Python...', 'plain', 'utf-8')
#如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？
#方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

import smtplib
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)#用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
server.login(from_addr,password)#login()方法用来登录SMTP服务器
server.sendmail(from_addr,[to_addr],msg.as_string())#sendmail()方法就是发邮件
server.quit()