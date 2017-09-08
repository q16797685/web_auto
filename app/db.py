#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 数据库连接
"""

from mysql import connector


# 获取数据库DB连接
conn = connector.connect(host='localhost', user='root', passwd='123456', db='autotest_platform', port=3306)
cur = conn.cursor()
# 数据库语句


