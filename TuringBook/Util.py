__author__ = 'xuezenghan'

import re
from TuringBook import Book
from urllib.request import urlopen,Request

def getBookFormHTML(BookUrl):

    # book = Book.book()
    HtmlPage = urlopen(Request(BookUrl)).read().decode("utf-8")


    #获取书名
    patternStr3 = r"<h1>(.*?)<\/h1>"
    BookNameStr = re.compile(patternStr3).findall(HtmlPage)
    # book.Name = BookNameStr[0]
    bookName = BookNameStr[0]


    #获取打折后电子书价格
    patternStr4 = r"&yen;\s+(.*?)<"
    BookNewPriceStr = re.compile(patternStr4).findall(HtmlPage)
    # print(BookNewPriceStr)
    BookPrice = BookNewPriceStr[0]


    #获取图片URL
    BookId = BookUrl.split("/")[-1]
    # print(BookId)
    patternStr5 = r"<img\ssrc=\"(.*?"+BookId+".*?)\""
    BookCoverStr = re.compile(patternStr5).findall(HtmlPage)
    BookCoverURLA = "http://www.ituring.com.cn/" + BookCoverStr[0]
    # print(BookCoverURL)


    #获取原价
    #      <div class="alert">
    # 2015年8月31日即恢复原价24.99，还在半价的有《Linux系统架构和应用技巧》<a href='http://www.ituring.com.cn/book/1097'>http://www.ituring.com.cn/book/1097</a>
    #    </div>

    patternStr6 = r"<div\sclass=\"alert\">\r\n\s*(.*?)<\/a>"
    InfoAreaStr = re.compile(patternStr6).findall(HtmlPage)
    # print(InfoAreaStr)

    #原价
    patternStr7 = r"\d+\.\d{2}"
    BookPriceStr = re.compile(patternStr7).findall(InfoAreaStr[0])
    # print(BookPriceStr)

    #另一本半价书的入口
    anotherEnterURL = InfoAreaStr[0].split(">")[1]

    book = Book.book(Name=bookName,price=BookPriceStr[0],BookCoverURL=BookCoverURLA,NewPrice=BookNewPriceStr[0])

    return book,anotherEnterURL



