"""
    Created by cala at 2019-10-25
"""

from app.libs.http_tool import HTTP
from flask import current_app

# connect local mysql
# 1.terminal: mysql.server start
# 2.open navicat and connect
class MyPandaLook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = MyPandaLook.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = MyPandaLook.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_state(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_state(page):
        return (page-1)*current_app.config['PER_PAGE']

