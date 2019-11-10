"""
    Created by cala at 2019-10-31
"""

from app.models.base import Base
from app.spider.panda_book import PandaBook
from app import db

from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, desc, func
from sqlalchemy.orm import relationship



class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        """
        :param uid:
        :return [isbn] of uid
        """
        user_wishes = Wish.query\
            .filter_by(uid=uid, launched=False)\
            .order_by(desc(Wish.create_time))\
            .all()
        return user_wishes

    @classmethod
    def get_gifts_count(cls, isbn_list):
        """
        select count(id), isbn from Wish where launched = False and isbn in ('','') and status = 1 group by isbn;
        :param isbn_list: [isbn]
        :return: [count] of [isbn]
        """
        # wishes_count_list = [len(Wish.query.filter_by(isbn=isbn, launched=False).all()) for isbn in isbn_list]

        from app.models.gift import Gift
        gifts_count_list = db.session.query(func.count(Gift.id), Gift.isbn)\
            .filter(Gift.launched == False, Gift.isbn.in_(isbn_list), Gift.status == 1)\
            .group_by(Gift.isbn)\
            .all()
        # tuple -> dict_list
        gifts_count_list = [{'count':item[0],
                              'isbn':item[1]} for item in gifts_count_list]

        return gifts_count_list

    @property
    def book(self):
        panda_book = PandaBook()
        panda_book.search_by_isbn(self.isbn)
        return panda_book.first