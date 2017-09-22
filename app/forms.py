# -*- coding: utf-8 -*-
# @Author: jun
# @Date:   2017-09-22 21:07:28
# @Last Modified by:   jun
# @Last Modified time: 2017-09-22 22:56:44

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
