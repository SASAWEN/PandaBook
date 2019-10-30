"""
    Created by cala at 2019-10-26
"""

from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    print('---',db)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)