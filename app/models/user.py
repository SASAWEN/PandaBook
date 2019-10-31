"""
    Created by cala at 2019-10-31
"""
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base
from app import login_manager

from sqlalchemy import Column, Integer, String, Boolean, Float

from flask_login import UserMixin

class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128))
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    recv_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        print(raw_password)
        print(generate_password_hash(raw_password))
        print(self.password)
        print(check_password_hash(self._password, raw_password))
        return check_password_hash(self._password, raw_password)

    def get_id(self):
        return self.id

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

