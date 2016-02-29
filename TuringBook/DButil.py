__author__ = 'xuezenghan'


import sqlite3
import os
import TuringBook.Book


DB_File_PATH = "E:\\Users\\xuezenghan\\PycharmProjects\\Turing\\Book.db"


def init():

    if not os.path.exists(DB_File_PATH):
        db = sqlite3.connect(DB_File_PATH)
        cur = db.cursor()
        cur.execute("CREATE TABLE books(id integer primary key ,"
                    "bookName VARCHAR(200) NOT NULL ,"
                        "price INTEGER NOT NULL,NewPrice INTEGER NOT NULL,BookCoverURL VARCHAR(200) NOT NULL ,"
                        "dateTime DATETIME DEFAULT(date('now')))")

        cur.close()
        db.close()




def get_conn():
    conn = sqlite3.connect(DB_File_PATH)

    return conn




def saveBook(conn,book):
    try:
        bookJson = book.toJson()
        print(bookJson)
        bookstr = (bookJson["BookName"],bookJson["price"],bookJson["NewPrice"],bookJson["BookCoverURL"])
        cur = conn.cursor()

        cur.execute("INSERT INTO books(bookName , price ,NewPrice,BookCoverURL) VALUES (?,?,?,?)",bookstr)
        cur.close()
        conn.commit()

    except Exception as e:
        print(e)
        return False

    return True



def searchBook(conn):

    bookresult =[]
    cur = conn.cursor()
    cur.execute("select bookName , price ,NewPrice,BookCoverURL from books order by dateTime DESC limit 2")
    for eachBook in cur.fetchall():
        print(eachBook)
        bookresult.append(eachBook)

    cur.close
    return bookresult


def closeDB(conn):
    conn.close()







