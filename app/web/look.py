"""
    Created by cala at 2019-10-25
"""

from flask import make_response, jsonify, request
from app.libs.handler import is_isbn_or_key
from app.spider.my_panda_look import MyPandaLook
from . import web
from app.forms.look import SearchForm

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

@web.route('/look/search')
def search():
    """
        q: 查询关键字（普通关键字，isbn编号）
        page:
    :return:
    """
    # args字典不可变
    # 转可变字典：a = request.args.to_dict()

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = MyPandaLook.search_by_isbn(q)
        else:
            result = MyPandaLook.search_by_keyword(q, page)
        #     jsonify 字符串转json
        return jsonify(result)
    else:
        return jsonify({form.errors})

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

