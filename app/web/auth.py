from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.libs.mail import send_email
from app.models.base import db
from app.models.user import User
from app.web import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        print(user.password)
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            print(next)
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    # 首先处理GET请求，直接render一个页面
    # 然后处理POST
    form = EmailForm(request.form)
    print(form.validate())
    print(request.method)
    if request.method == 'POST' and form.validate():
        account_email = form.email.data
        user = User.query.filter_by(email=account_email).first_or_404()
        # TODO: send_email连接邮件服务器，反应时间，考虑异步发送邮件（邮件实时性 < 页面跳转实时性
        send_email(account_email, "重置密码", 'email/reset_password.html', user = user, token=user.generate_token())
        flash('重置密码邮件已发送！')
    return render_template('auth/forget_password_request.html', form = form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    # use token : save user id, identify which user
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash('密码更新成功！')
            return redirect(url_for('web.login'))
        else:
            flash('密码重置失败！')
    return render_template('auth/forget_password.html', form = form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
    pass


@web.route('/register/confirm/<token>')
def confirm(token):
    pass


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    pass


