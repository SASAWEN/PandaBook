
from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import desc, or_

from app.forms.book import TradingForm
from app.libs.mail import send_email
from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.trading import Trading
from app.models.gift import Gift
from app.models.user import User
# from app.models.wish import Wish
from app.view_models.book import BookViewModel
from app.view_models.trading import TradingCollection
from app.web import web



@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)
    # 1. one can't send a gift to himself
    if current_gift.is_yourself_gift(current_user.id):
        flash('不可以向自己所要书籍哦～')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    if not current_user.can_send_book():
        return render_template('not_enough_beans.html', beans=current_user.beans)

    # send email to inform the sender that someone wants the book
    form = TradingForm(request.form)
    print(form.recipient_name)
    if request.method == 'POST' and form.validate():
        save_drift(form, current_gift)
    #     send email
        send_email(current_gift.user.email,
                   'Someone wants your book',
                   'email/get_gift.html',
                   wisher=current_user,
                   gift=current_gift)
        return redirect(url_for('web.pending'))

    sender = current_gift.user.summary
    return render_template('drift.html', gifter=sender, user_beans=current_user.beans, form=form)

@web.route('/pending')
@login_required
def pending():
    tradings = Trading.query.filter(or_(Trading.sender_id==current_user.id,
                                    Trading.receiver_id==current_user.id)).order_by(
        desc(Trading.create_time)).all()
    views = TradingCollection(tradings, current_user.id)
    return render_template('pending.html', drifts=views.data)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    """
        拒绝请求，只有书籍赠送者才能拒绝请求
        注意需要验证超权
    """
    pass
    # with db.auto_commit():
    #     drift = Drift.query.filter(Gift.uid==current_user.id,
    #                                Drift.id==did).first_or_404()
    #     drift.pending = PendingStatus.Reject
    #     requester = User.query.get_or_404(drift.requester_id)
    #     requester.beans += 1
    # return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/redraw')
@login_required
def redraw_drift(did):
    """
        撤销请求，只有书籍请求者才可以撤销请求
        注意需要验证超权
    """
    pass
    # with db.auto_commit():
    #     # 超权 获取到登录权限后，修改了did来修改他人的信息
    #     drift = Drift.query.filter_by(requester_id=current_user.id,id=did).first_or_404()
    #     drift.pending = PendingStatus.Redraw
    #     current_user.beans += 1
    # return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
    """
        确认邮寄，只有书籍赠送者才可以确认邮寄
        注意需要验证超权
    """
    pass
    # with db.auto_commit():
    #     drift = Drift.query.filter_by(gifter_id=current_user.id, id=did).first_or_404()
    #     drift.pending = PendingStatus.Success
    #     current_user.beans += 1
    #     gift = Gift.query.filter_by(id=drift.requester_id).first_or_404()
    #     gift.launched = True
    #     # 完成邮寄，更新wish的launched
    #     Wish.query.filter_by(isbn=drift.isbn,
    #                          uid=drift.requester_id,launched=False).update({Wish.launched:True})
    # return redirect(url_for('web.pending'))


# 定义一个函数用来将鱼漂填写表单信息存入数据库
def save_drift(trading_form, current_gift):
    with db.auto_commit():
        trading = Trading()
        trading_form.populate_obj(trading)

        trading.gift_id = current_gift.id
        trading.sender_id = current_gift.user.id
        trading.sender_nickname = current_gift.user.nickname
        trading.receiver_id = current_user.id
        trading.receiver_nickname = current_user.nickname

        book = BookViewModel(current_gift.book)
        trading.book_title = book.title
        trading.book_author = book.author
        trading.book_img = book.image
        trading.isbn = book.isbn

        try:
            if current_user.beans <= 0:
                raise Exception
            current_user.beans -= 1
            db.session.add(trading)
        except Exception as e:
            print(e)
            pass
