#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#操作XML有两种方法：DOM和SAX。
#DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
#SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
#正常情况下，优先考虑SAX，因为DOM实在太占内存

#在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了
#举个例子，当SAX解析器读到一个节点时：
#<a href="/">python</a>
#会产生3个事件：
#start_element事件，在读取<a href="/">时；
#char_data事件，在读取python时；
#end_element事件，在读取</a>时。

#请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
#https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml

#参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

from xml.parsers.expat import ParserCreate
from urllib import request

class MySaxHandler(object):
     def __init__(self):
         self.result = dict(city=None, forecast=[])
     def start_element(self, name, attr):
         if attr.get("city"):
             self.result["city"] = attr["city"]
         if attr.get("date") and not attr.get("temp"):
             self.result["forecast"].append(dict(date=attr["date"], high=attr["high"],low=attr["low"]))

def parseXml(xml_str):
     parser = ParserCreate()
     handler = MySaxHandler()
     parser.StartElementHandler = handler.start_element
     parser.Parse(xml_str)
     return handler.result

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
	data = f.read()

result = parseXml(data.decode('utf-8'))
print (result)
assert result['city'] == 'Beijing'
