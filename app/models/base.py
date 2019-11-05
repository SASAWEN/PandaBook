"""
    Created by cala at 2019-10-31
"""

from sqlalchemy import SmallInteger, Column, Integer
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager
from datetime import datetime

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

class Query(BaseQuery):
    # 解决假删除 status=0
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    # database不创建Base表
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1) # 1 exist , 0 not exist

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    # fake delete
    def delete(self):
        self.status = 0

    def set_attrs(self, attr_dict):
        for key, value in attr_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)