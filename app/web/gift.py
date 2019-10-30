from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

# from app.libs.enums import PendingStatus
# from app.models.base import db
# from app.models.drift import Drift
# from app.models.gift import Gift
# from app.view_models.trade import MyTrades
from app.web import web


#装饰器login_required是login插件提供的权限管理插件，当没有读取到票据，也就没有权限访问视图函数
@web.route('/my/gifts')
@login_required
def my_gifts():
    pass
    # uid = current_user.id
    # gifts_of_mine = Gift.get_user_gifts(uid)
    # # 根据查询的礼物列表将每个礼物的isbn查询出来组成列表
    # gifts_isbn_list = [gift.isbn for gift in gifts_of_mine]
    # wish_count_list = Gift.get_wish_counts(gifts_isbn_list)
    # my_gifts_view_model = MyTrades(gifts_of_mine, wish_count_list)
    # return render_template('my_gifts.html', gifts=my_gifts_view_model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    pass
    # if current_user.can_save_to_list(isbn):
    #     with db.auto_commit():
    #         gift = Gift()
    #         gift.isbn = isbn
    #         gift.uid = current_user.id
    #         current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    #         db.session.add(gift)
    # else:
    #     flash('这本书已经存在于你的心愿清单或赠送清单，请勿重复添加！')
    # return redirect(url_for('web.book_detail', isbn = isbn))

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
