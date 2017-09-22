# -*- coding: utf-8 -*-
# @Author: jun
# @Date:   2017-09-21 15:12:49
# @Last Modified by:   jun
# @Last Modified time: 2017-09-21 15:48:43


from flask import Flask

app = Flask(__name__)
from app import views
