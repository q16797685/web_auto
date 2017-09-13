#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 数据库连接
"""

from mysql import connector


# mysql连接类
class MysqlConnect(object):
    # 获取数据库DB连接
    conn = connector.connect(host='localhost', user='root', passwd='123456', db='autotest_platform', port=3306)
    # 查询平台用户语句
    select_user_sql = "SELECT * FROM autotest_platform.user;"
    # 查询平台
    select_interface_name = "SELECT * FROM autotest_platform.interface;"




