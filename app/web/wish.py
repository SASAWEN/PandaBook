from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
# from werkzeug.contrib import limiter

# from app.libs.email import send_mail
# from app.models.base import db
# from app.models.gift import Gift
# from app.models.wish import Wish
# from app.view_models.trade import MyTrades
from app.web import web



def limit_key_prefix():
    pass

@web.route('/my/wish')
@login_required
def my_wish():
    pass
    # uid = current_user.id
    # wishes_of_mine = Wish.get_user_wishes(uid)
    # isbn_list = [wish.isbn for wish in wishes_of_mine]
    # gift_count_list = Wish.get_gifts_counts(isbn_list)
    # wishes_view_model = MyTrades(wishes_of_mine, gift_count_list)
    # return render_template('my_wish.html', wishes=wishes_view_model.trades)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    pass
    # if current_user.can_save_to_list(isbn):
    #     with db.auto_commit():
    #         wish = Wish()
    #         wish.isbn = isbn
    #         wish.uid = current_user.id
    #         db.session.add(wish)
    # else:
    #     flash('这本书已经存在于你的心愿清单或赠送清单，请勿重复添加！')
    # return redirect(url_for('web.book_detail', isbn = isbn))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    """
        向想要这本书的人发送一封邮件
        注意，这个接口需要做一定的频率限制
        这接口比较适合写成一个ajax接口
    """
    pass
    # wish = Wish.query.filter_by(id=wid,launched=False).first_or_404()
    # gift = Gift.query.filter_by(uid=current_user.id,
    #                             isbn=wish.isbn,launched=False).first()
    # if not gift:
    #     flash('你还没有上传此书，'
    #           '请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
    # else:
    #     send_mail(wish.user.email,
    #               '有人想送你一本书', 'email/satisify_wish.html', wish=wish,
    #               gift=gift)
    #     flash('已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
    # return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    pass
    # wish = Wish.query.filter_by(isbn=isbn,launched=False).first_or_404()
    # with db.auto_commit():
    #     wish.delete()
    # return redirect(url_for('web.my_wish'))

# @limiter.limited
def satifiy_with_limited():
    pass
    # isbn = request.args['isbn']
    # flash('你已向他发送过赠送邀请，请不要频繁发送')
    # return redirect(url_for('web.book_detail', isbn=isbn))