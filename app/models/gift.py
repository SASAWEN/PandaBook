"""
    Created by cala at 2019-10-31
"""
from flask import current_app

from app.models.base import Base
from app.spider.panda_book import PandaBook

from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, desc
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

    @property
    def book(self):
        panda_book = PandaBook()
        panda_book.search_by_isbn(self.isbn)
        return panda_book.first