"""
    Created by cala at 2019-10-26
"""

# 提供相关模版和文件

from flask import Blueprint

web = Blueprint('web', __name__, template_folder='templates')

# 导入视图函数
from app.web import book
from app.web import user
