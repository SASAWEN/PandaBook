from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

# from app.libs.enums import PendingStatus
from app.models.base import db
# from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.trade import MyTrades
# from app.view_models.trade import MyTrades
from app.web import web


# 装饰器login_required是login插件提供的权限管理插件，当没有读取到票据，也就没有权限访问视图函数
@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_list = Gift.get_user_gifts(uid)
    gifts_isbn = [gift.isbn for gift in gifts_list]
    gifts_wishes_count = Gift.get_wishes_count(gifts_isbn)
    my_gifts_view_model = MyTrades(gifts_list, gifts_wishes_count)
    return render_template('my_gifts.html', gifts=my_gifts_view_model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # commit 执行才被写入数据库
        # rollback 事务回滚 防止因事务操作发生错误 sqlalchemy无法进行下一次数据库操作
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
        print(gift)
        return redirect(url_for('web.book_detail'), book=gift)
    else:
        flash('请勿将同一本书加入心愿清单和赠送清单！')

    # return redirect(url_for('web.book_detail'), isbn=isbn)


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass
    # gift = Gift.query.filter_by(id=gid,launched=False).first_or_404()
    # drift = Drift.query.filter_by(gift_id=gid, pending=PendingStatus.Waiting).first()
    # if drift:
    #     flash('这个礼物正处于交易状态，请先去鱼漂中完成该交易')
    # else:
    #     with db.auto_commit():
    #         current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
    #         gift.delete()
    # return redirect(url_for('web.my_gifts'))
