# -*- coding: utf-8 -*-
# @Author: jun
# @Date:   2017-09-22 17:39:08
# @Last Modified by:   jun
# @Last Modified time: 2017-09-22 22:39:03

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess-hahaha'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.Yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
