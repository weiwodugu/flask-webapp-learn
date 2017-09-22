# -*- coding: utf-8 -*-
# @Author: jun
# @Date:   2017-09-21 15:15:19
# @Last Modified by:   jun
# @Last Modified time: 2017-09-21 16:12:29

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movies was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
