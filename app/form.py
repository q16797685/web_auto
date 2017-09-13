#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 表单方法
"""

from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterInterface(Form):
    register_username = StringField(u'用户名', validators=[DataRequired(), Length(5, 12, message=u'用户名长度在6到12为')])
    register_password = PasswordField(u'密码', validators=[DataRequired(), Length(6, 12, message=u'密码长度在6到12为')])
    register_twice_password = PasswordField(u'再次密码', validators=[DataRequired(), Length(6, 12, message=u'密码长度在6到12为'), EqualTo('register_password', message=u'密码必须一致')])
    register_submit = SubmitField('submit')


class LoginInterface(Form):
    login_username = StringField('username', validators=[DataRequired()])
    login_password = PasswordField('password', validators=[DataRequired()])
    Login_submit = SubmitField('submit')


class AddInterface(Form):
    interface_name = StringField(u'接口名称', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口名称'})
    interface_url = StringField(u'接口地址', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口地址'})
    interface_methods = SelectField(u'接口方法', validators=[DataRequired()], choices=[('POST', 'post'), ('GET', 'get')])
    # interface_parameter = StringField(u'接口参数', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口参数'})
    # interface_parameter = StringField(u'接口返回参数', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口参数'})
    interface_submit = SubmitField('submit')
