"""
    Created by cala at 2019-10-29
"""
from sqlalchemy import Column,Integer, String
from flask_sqlalchemy import SQLAlchemy

# 模型层
# 数据库访问库：
# sqlalchemy
# Flask_SQLAlchemy 底层sqlalchemy实现
# WTFORMS
# FLask_WTFORMS

db = SQLAlchemy()
print('look',db)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# 继承Model类
class look(db.Model):
    __tablename__ = 'look'
    # 字段声明，可指定主键
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(50), nullable=False)
    author = db.Column(String(30), default='匿名')
    isbn = db.Column(String(15), nullable=False, unique=True)
    publisher = db.Column(String(50))
    image = db.Column(String(50))
    summary = db.Column(String(1000))
    update = db.Column(String(20))
    price = db.Column(String(20))
    binding = db.Column(String(20))
    pages = db.Column(Integer)
    print('look loaded')
    def sample(self):
        pass

