"""
    Created by cala at 2019-10-24
"""


from app import create_app

app = create_app()


if __name__ == '__main__':
    # 生产环境下使用nginx+uwsgi部署
    # nginx：前置服务器，处理前端请求
    # uwsgi：Flask自带web服务器加载模块，因此生产环境下不会进入'__main__'，不会执行run
    # debug=True不需要重新加载flask，可以自动同步代码
    # app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
    app.run(debug=app.config['DEBUG'])
    print("jesus")
