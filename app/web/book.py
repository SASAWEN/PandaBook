"""
    Created by cala at 2019-10-25
"""

from flask import make_response, jsonify, request, render_template, flash
from flask_login import current_user

from app.libs.handler import is_isbn_or_key
from app.spider.panda_book import PandaBook
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeInfo
from app.models.gift import Gift
from app.models.wish import Wish
import json
# request由http请求触发


# 参数合法验证：
# 长度限制
# 类型验证（正整数，MAX限制）

# 验证方式：
# 1.直接在视图函数验证（不
# 2.封装到函数中（不
# 3.三方插件wtforms自动校验

# 最佳方式：建立验证层
# wtforms自动校验

@web.route('/book/search')
def search():
    """
        q: 查询关键字（普通关键字，isbn编号）
        page:
    :return:
    """
    # args字典不可变
    # 转可变字典：a = request.args.to_dict()

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        panda_book = PandaBook()
        if isbn_or_key == 'isbn':
            panda_book.search_by_isbn(q)
        else:
            panda_book.search_by_keyword(q, page)

        books.fill(panda_book, q)
        # return json.dumps(books, default=lambda o:o.__dict__, ensure_ascii=False)
    else:
        flash('Searching format error.')
    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
    search result -> click book -> book detail
    has_in_gifts/has_in_wishes: is gift or wish of current user
    :param isbn:
    :return:
    """
    has_in_gifts = False
    has_in_wishes = False

    panda_book = PandaBook()
    panda_book.search_by_isbn(isbn)
    book = BookViewModel(panda_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    # fetch user list
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book, wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_wishes=has_in_wishes, has_in_gifts=has_in_gifts)

# 视图函数 view func
# 与一般函数区别在于：
# content-type http headers
# 返回Resonse对象
@web.route('/hello/<name_>')
def hello_panda(name_):
    headers = {
        # content-type = text/html 返回值类型为html标签格式
        # 返回值类型为普通文本
        'content-type':'text/plain',
        # location 重定向url
        'location':'http://baidu.com'

    }

    # 相当于返回三元组，flask内部重组成一个response对象，与下面代码效果相同
    # return '<html></html>', 301, headers

    # 301 重定向
    response = make_response('<html></html>', 200)
    response.headers = headers
    return response

