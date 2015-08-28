__author__ = 'xuezenghan'

import json

class book():

    Name = ""
    price = 0
    NewPrice = 0

    def __init__(self,Name,price,NewPrice,BookCoverURL):
        self.Name = Name
        self.price = price
        self.NewPrice = NewPrice
        self.BookCoverURL = BookCoverURL



    def toJson(self):
        jsonDate = []
        jsonDate["BookName"] = self.Name
        jsonDate["price"] = self.price
        jsonDate["NewPrice"] = self.NewPrice
        jsonDate["BookCoverURL"] = self.BookCoverURL

        return jsonDate
