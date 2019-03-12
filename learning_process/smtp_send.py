#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件

#首先，我们来构造一个最简单的纯文本邮件：
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

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
#msg = MIMEText('<html><body><h1>Hello</h1>' +
#    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#    '</body></html>', 'html', 'utf-8')
#如果Email中要加上附件怎么办？
#带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
#所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
#再继续往里面加上表示附件的MIMEBase对象即可

#如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？
#办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。
#利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

#如果要把一个图片嵌入到邮件正文中怎么做？
#直接在HTML邮件中链接图片地址行不行？答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
#要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
#如果有多个图片，给它们依次编号，然后引用不同的cid:x即可
#邮件正文是MIMEText:
#msg.attach(MIMEText('<html><body><h1>Hello</h1>'+
#	'<p><img src="cid:0"></p>'+
#	'</body></html>', 'html', 'utf-8'))

#添加附件就是加上一个MIMEBase，从本地读取一个图片:
#with open('C:/Users/jingoal/MyPython/learning_process/2523reopen0510.png','rb') as f:
#	#设置附件的MIME和文件名，这里是png类型:
#	mime=MIMEBase('image','png',filename='2523reopen0510.png')
#	#加上必要的头信息:
#	mime.add_header('Content-Disposition','attachment',filename='2523reopen0510.png')
#	mime.add_header('Content-ID','<0>')
#	mime.add_header('X-Attachment-Id','0')
#	#把附件的内容读进来:
#	mime.set_payload(f.read())
#	# 用Base64编码:
#	encoders.encode_base64(mime)
#	# 添加到MIMEMultipart:
#	msg.attach(mime)




import smtplib
#使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。
#要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)#用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
server.login(from_addr,password)#login()方法用来登录SMTP服务器
server.sendmail(from_addr,[to_addr],msg.as_string())#sendmail()方法就是发邮件
server.quit()