"""
    Created by cala at 2019-10-29
"""
from sqlalchemy import Column,Integer, String
from app.models.base import Base
# 模型层
# 数据库访问库：
# sqlalchemy
# Flask_SQLAlchemy 底层sqlalchemy实现
# WTFORMS
# FLask_WTFORMS

# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# 继承Model类
class Book(Base):
    __tablename__ = 'book'
    # 字段声明，可指定主键
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='匿名')
    isbn = Column(String(15), nullable=False, unique=True)
    publisher = Column(String(50))
    image = Column(String(50))
    summary = Column(String(1000))
    pubdate = Column(String(20))
    price = Column(String(20))
    binding = Column(String(20))
    pages = Column(Integer)
    print('book loaded')
    def sample(self):
        pass

