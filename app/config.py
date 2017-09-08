#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 配置页面,防止A secret key is required to use CSRF
"""


from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

CSRF_ENABLED = True
SECRET_KEY = "you-will-never-guess"

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/autotest_platform'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)