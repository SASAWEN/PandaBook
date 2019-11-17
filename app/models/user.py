"""
    Created by cala at 2019-10-31
"""

from math import floor
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.handler import is_isbn_or_key
from app.libs.enums import PendingStatus

from app.models.base import Base
from app.models.gift import Gift
from app.models.wish import Wish
from app.models.trading import Trading

from app import login_manager, db

from sqlalchemy import Column, Integer, String, Boolean, Float

from flask import current_app
from flask_login import UserMixin

from app.spider.panda_book import PandaBook


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
        return check_password_hash(self._password, raw_password)


    def generate_token(self, expiration=600):
        """
            use itsdangerous to generate token
            param: expiration: 600s valid time
        """
        # 序列化器
        s = Serializer(secret_key=current_app.config['SECRET_KEY'], expires_in=expiration)
        # byte list -> string, id can be other message
        token = s.dumps({'id': self.id}).decode('utf-8')
        return token


    @classmethod
    def reset_password(cls, token, new_password):
        # password(new_password)
        s = Serializer(secret_key=current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            print('序列化token加载异常')
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get_or_404(uid)
            if user:
                user.password = new_password
            else:
                print('用户不存在！')
                return False
        return True

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False

        panda_book = PandaBook()
        panda_book.search_by_isbn(isbn)
        if not panda_book.first:
            return False

        # user can not gifting and wishing the same book at the same time

        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        return not gifting and not wishing

    def can_send_book(self):
        """
        1. beans
        2. how many books have been sent
        3. how many books have been received
        ask for 2 send 1
        :return:
        """
        if self.beans < 1:
            return False

        success_send = Gift.query.filter_by(
            uid = self.id,
            launched = True
        ).count()

        success_trade = Trading.query.filter_by(
            sender_id = self.id,
            pending = PendingStatus.Success
        ).count()

        return floor(success_send/2) >= success_trade

    def get_id(self):
        return self.id

    @property
    def summary(self):
        # can be use to describe trading info
        return dict(
            nickname = self.nickname,
            beans = self.beans,
            email = self.email,
            send_receive = str(self.send_counter) + '/' + str(self.recv_counter)
        )


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

