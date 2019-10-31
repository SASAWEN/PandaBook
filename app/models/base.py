"""
    Created by cala at 2019-10-31
"""

from sqlalchemy import SmallInteger, Column
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Base(db.Model):
    # database不创建Base表
    __abstract__ = True
    # create_time = Column()
    status = Column(SmallInteger, default=1) # 1 exist , 0 not exist

    def set_attrs(self, attr_dict):
        for key, value in attr_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)