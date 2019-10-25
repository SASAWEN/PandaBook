"""
    Created by cala at 2019-10-24
"""


from flask import Flask, make_response, jsonify
from handler import is_isbn_or_Key
from my_panda_look import MyPandaLook


app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/book/seaerch/<q>/<page>')
def search(q, page):
    """
        q: 查询关键字（普通关键字，isbn编号）
        page:
    :return:
    """
    isbn_or_key = is_isbn_or_Key(q)
    if isbn_or_key == 'isbn':
        result = MyPandaLook.search_by_isbn(q)
    else:
        result = MyPandaLook.search_by_keyword(q)
    #     jsonify 字符串转json
    return jsonify(result)

# 视图函数 view func
# 与一般函数区别在于：
# content-type http headers
# 返回Resonse对象
@app.route('/hello/<name_>')
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
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


if __name__ == '__main__':
    # 生产环境下使用nginx+uwsgi部署
    # nginx：前置服务器，处理前端请求
    # uwsgi：Flask自带web服务器加载模块，因此生产环境下不会进入'__main__'，不会执行run
    # debug=True不需要重新加载flask，可以自动同步代码
    # app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
    app.run(debug=app.config['DEBUG'])
    print("jesus")
