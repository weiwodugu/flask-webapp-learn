# -*- coding: utf-8 -*-
# @Author: jun
# @Date:   2017-09-21 15:12:49
# @Last Modified by:   jun
# @Last Modified time: 2017-09-22 21:02:55


from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
from app import views
