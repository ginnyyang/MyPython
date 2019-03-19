#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base =declarative_base()

# 定义User对象,User拥有多个Book
class User(Base):
	# 表的名字:
	__tablename__='user'
	
	# 表的结构:
	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	# 一对多:
	books=relationship('Book')

class Book(Base):
	__tablename__='book'
	
	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	# “多”的一方的book表是通过外键关联到user表的
	user_id=Column(String(20),ForeignKey('user.id'))
	
# 初始化数据库连接--'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')

# 创建DBSession类型:
DBSession=sessionmaker(bind=engine)

#向数据库表中添加一行记录
# 创建session对象
session=DBSession()
# 创建新User对象:
new_user=User(id='2',name='yangjing2')

session.add(new_user)# 添加到session:
session.commit()# 提交即保存到数据库:
session.close()# 关闭session:

#查询数据
session=DBSession()
user = session.query(User).filter(User.id=='2').one()
print('type:',type(user))
print('name:',user.name)
session.close()