"""
    Created by cala at 2019-10-28
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp

# search参数校验
class SearchForm(Form):
    q = StringField(validators=[
        DataRequired(), Length(min=1, max=30)])

    page = IntegerField(validators=[
        NumberRange(min=1, max=99)], default=1)


class TradingForm(Form):
    recipient_name = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称为2-10个字符')])

    mobile = StringField(validators=[
        DataRequired(), Regexp ('^1[0-9]{10}$', 0, '请输入正确的手机号')])

    message = StringField()

    address = StringField(validators=[
        DataRequired(), Length(10, 70, message='地址不能低于10个字')])