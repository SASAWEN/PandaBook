"""
    Created by cala at 2019-10-26
"""

from flask import Flask
from flask_login import LoginManager
from app.models.base import db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    db.create_all(app=app)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    print('---',db)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)