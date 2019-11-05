"""
    Created by cala at 2019-10-31
"""
from flask import current_app

from app.models.base import Base
from app.models.wish import Wish
from app.spider.panda_book import PandaBook
from app import db

from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, desc, func
from sqlalchemy.orm import relationship



class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def recent(cls):
        recent_gifts = Gift.query\
            .filter_by(launched=False)\
            .order_by(desc(Gift.create_time))\
            .limit(current_app.config['RECENT_BOOK_COUNT'])\
            .distinct().all()
        return recent_gifts

    @classmethod
    def get_user_gifts(cls, uid):
        """
        :param uid:
        :return [isbn] of uid
        """
        user_gifts = Gift.query\
            .filter_by(uid=uid, launched=False)\
            .order_by(desc(Gift.create_time)).all()
        return user_gifts

    @classmethod
    def get_wishes_count(cls, isbn_list):
        """
        select count(id), isbn from Wish where launched = False and isbn in ('','') and status = 1 group by isbn;
        :param isbn_list: [isbn]
        :return: [count] of [isbn]
        """
        # wishes_count_list = [len(Wish.query.filter_by(isbn=isbn, launched=False).all()) for isbn in isbn_list]

        wishes_count_list = db.session.query(func.count(Wish.id), Wish.isbn)\
            .filter(Wish.launched == False, Wish.isbn.in_(isbn_list), Wish.status == 1)\
            .group_by(Wish.isbn).all()
        # tuple -> dict_list
        wishes_count_list = [{'count':item[0],
                              'isbn':item[1]} for item in wishes_count_list]

        return wishes_count_list

    @property
    def book(self):
        panda_book = PandaBook()
        panda_book.search_by_isbn(self.isbn)
        return panda_book.first