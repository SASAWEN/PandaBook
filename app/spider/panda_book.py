"""
    Created by cala at 2019-10-25
"""

from app.libs.http_tool import HTTP
from flask import current_app

# connect local mysql
# 1.terminal: mysql.server start
# 2.open navicat and connect

# MVC Model层
# fetch data from yushu website
#
class PandaBook:
    # class params
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        # object params
        # search for one book or several books => save book(s) as a list and length of the list
        # param:
        # books: book list
        # total: length of the list
        self.total = 0
        self.books = []

    # single book search from yushu website
    def search_by_isbn(self, isbn):
        # self.param 查找：实例变量 -> 类变量
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        print(result)
        self.__fill_single(result)
        # TODO: save to database
        return result

    # set search from yushu website
    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_state(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        return result

    # set object params
    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)
        pass

    # set object params
    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']
        pass

    # calculate the first book No. in the current page
    def calculate_state(self, page):
        return (page-1)*current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
