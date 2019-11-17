"""
    Created by cala at 2019-11-17
"""

from app import mail
from flask_mail import Message
from flask import current_app, render_template

from threading import Thread

def send_async_email(curr_app, msg):
    with curr_app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            print('邮件发送失败')
            pass

def send_email(to, subject, template, **kargs):
    msg = Message(current_app.config['MAIL_SUBJECT_PREFIX']+' '+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to],
                  html = render_template(template, **kargs))
    thr_send = Thread(target=send_async_email, args=[current_app._get_current_object(), msg])
    thr_send.start()

