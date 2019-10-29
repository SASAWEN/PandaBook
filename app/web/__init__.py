"""
    Created by cala at 2019-10-26
"""

# 提供相关模版和文件

from flask import Blueprint

web = Blueprint('web', __name__)

# 导入视图函数
from app.web import look
from app.web import user
