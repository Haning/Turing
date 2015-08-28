__author__ = 'xuezenghan'


import urllib.request
import re
from TuringBook import Util
import sqlite3

BaseUrl = "http://www.ituring.com.cn/"

BookURLList = []

PageDate = urllib.request.urlopen(urllib.request.Request(BaseUrl)).read().decode("utf-8")

#print(PageDate)

#半价书入口
# <dt><a href="http://www.ituring.com.cn/book/1320"><img src="http://www.ituring.com.cn/html/office/icon/ebookcoupon.png" />电子书每周半价</a></dt>
patternStr1 = r"<\s*a.*?>.*电子书每周半价<\s*/\s*a\s*>"
EnterStr = re.compile(patternStr1).findall(PageDate)[0]

#获取入口URL
EnterUrl = EnterStr.split("\"")[1]
BookURLList.append(EnterUrl)

#进入URL获取书名，价格、图片链接、另一个半价入口。
#书名 <h1>Scala与Clojure函数式编程模式：Java虚拟机高效编程</h1>
#价格
#<div class="alert">
# 2015年8月31日即恢复原价24.99，还在半价的有《Linux系统架构和应用技巧》
# <a href="http://www.ituring.com.cn/book/1097">http://www.ituring.com.cn/book/1097</div>

print(EnterUrl)

BookA,anotherEnterUrl = Util.getBookFormHTML(EnterUrl)

print(BookA.Name)

if not anotherEnterUrl in BookURLList:
    BookURLList.append(anotherEnterUrl)
    BookB,ananotherBook = Util.getBookFormHTML(anotherEnterUrl)
    print(BookB.Name)

#存储

