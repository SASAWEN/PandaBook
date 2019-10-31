"""
    Created by cala at 2019-10-31
"""

from wtforms import Form, StringField, ValidationError
from wtforms.validators import Length, DataRequired, Email

from app.models.user import User

class RegisterForm(Form):
    email = StringField(validators=[
        DataRequired(), Length(8, 64), Email(message='邮箱格式不符合规范')])

    password = StringField(validators=[
        DataRequired(message='密码不能为空'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称为2-10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')
