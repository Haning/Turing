__author__ = 'xuezenghan'


import sqlite3
import os
import TuringBook.Book


DB_File_PATH = "\Book.db"


def init():
    if(os.)



def get_conn():
    conn = sqlite3.connect(DB_File_PATH)

    return conn




def saveBook(conn,book):
    book.toJson()