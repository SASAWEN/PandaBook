"""
    Created by cala at 2019-11-17
"""

"""
    交易记录模型
"""

from app import db
from app.models.base import Base
from app.libs.enums import PendingStatus

from sqlalchemy import Column, Integer, String, SmallInteger

class Trading(Base):

    id = Column(Integer, primary_key=True, autoincrement=True)

    # trading status
    pending = Column(SmallInteger, default=1)

    # deliver
    recipient_name = Column(String(24), nullable=False)
    address = Column(String(100), nullable=False)
    mobile = Column(String(20), nullable=False)
    message = Column(String(200))

    # sender
    gift_id = Column(Integer)
    sender_id = Column(Integer)
    sender_nickname = Column(String(24), nullable=False)

    # receiver
    receiver_id = Column(Integer)
    receiver_nickname = Column(String(24), nullable=False)

    # book info
    isbn = Column(String(15), nullable=False)
    book_title = Column(String(50), nullable=False)
    book_author = Column(String(30), default='匿名')
    book_img = Column(String(50))