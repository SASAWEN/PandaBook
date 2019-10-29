"""
    Created by cala at 2019-10-26
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.look import web
    app.register_blueprint(web)