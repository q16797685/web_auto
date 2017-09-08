#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 数据库模型
"""

import config


class Role(config.db.Model):
    __tablename__ = 'roles'
    id = config.db.Column(config.db.Integer, primary_key=True)
    name = config.db.Column(config.db.String(64), unique=True)
    def __repr__(self):
        return '<Role %r>' % self.name


class User(config.db.Model):
    __tablename__ = 'users'
    id = config.db.Column(config.db.Integer, primary_key=True)
    username = config.db.Column(config.db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username