from flask import render_template

# from app.models.gift import Gift
from app.view_models.book import BookViewModel
from app.web import web


__author__ = '七月'


# def __current_user_status_change():
#     r = request


@web.route('/')
# @cache.cached(timeout=100, unless=__current_user_status_change)
# @cache.cached(timeout=100)
def index():
    """
        首页视图函数
        这里使用了缓存，注意缓存必须是贴近index函数的
    """
    return "hello"
    # recent_gifts = Gift.recent()
    # books = [BookViewModel(gift.book) for gift in recent_gifts]
    # return render_template('index.html',recent = books)

@web.route('/personal')
def personal_center():
    pass

