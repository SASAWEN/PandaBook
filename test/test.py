"""
    Created by cala at 2019-10-29
"""

from flask import Flask, current_app

app = Flask(__name__)

# 应用上下文对象 Flask AppContext
# 请求上下文对象 Request RequestContext
# http请求使用current_app不需要手动push Flask内部检测并push app
# 写离线应用、但愿测试时 需要手动push应用上下文 app
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# with语句：
# 1.实现了上下文协议的对象——上下文管理器 AppContext
# 2.实现了"__enter__"和"__exit__"方法
# 3.实现上下文表达式——返回上下文管理器 app_context()

# with xx as obj:
# obj 是"__enter__"方法返回对象

# "__exit__"方法 回收资源
# 参数（self, exc_type, exc_value, tb)
# 正常执行，exc_type, exc_value, tb为空
# 发生异常，exc_type 异常类型，tb 详细信息
# 返回值 True：with语句外不抛出异常 False：with语句外抛出异常

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']


