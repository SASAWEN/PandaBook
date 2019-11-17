"""
    Created by cala at 2019-10-26
"""

# 提供相关模版和文件

from flask import Blueprint, render_template

web = Blueprint('web', __name__, template_folder='templates')

@web.app_errorhandler(404)
def not_found(e):
    # TODO: write log
    return render_template('404.html'), 404

# 导入视图函数
from app.web import book
from app.web import auth
from app.web import trading
from app.web import gift
from app.web import wish
from app.web import main