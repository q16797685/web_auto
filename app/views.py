#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 页面视图方法
"""


from flask import Flask,render_template,request,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from form import RegisterInterface, AddInterface
import db


WEATHERS = {'cityname': u'上海',
            'cityno': '101280601'}


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = u'主页', user = user, posts = posts, current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.route('/wether')
def wether_information():
    return render_template('wether.html', current_time=datetime.utcnow(), weathers = WEATHERS, wether_title = u'天气预报')


# @app.route('/login', methods=['GET'])
# def login_form():
#     return render_template('login.html')


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = db.conn.cursor()
        select_user_sql = "SELECT * FROM autotest_platform.user;"
        cur.execute(select_user_sql)
        data = cur.fetchall()
        for username_data in data:
            if username_data[0] == username:
                if username_data[1] == password:
                    return redirect(url_for('main_form'))
                else:
                    return render_template('login.html', message=u'请输入正确密码')
            else:
                continue
        return render_template('login.html', message=u'请输入正确用户名')


@app.route('/main', methods=['GET'])
def main_form():
    return render_template('main.html')


# @app.route('/register', methods=['GET'])
# def register():
#     register_form = RegisterInterface()
#     return render_template('register.html', form = register_form)


@app.route('/register', methods=['POST','GET'])
def register_form():
    form = RegisterInterface()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user_name = request.form['register_username']
            user_password = request.form['register_password']
            cur = db.conn.cursor()
            # insert_user_sql = "insert into user (username,password) values(%s,%s)",(user_name, user_password)  #插入SQL
            cur.execute("insert into user (username,password) values(%s,%s)",(user_name, user_password))
            db.conn.commit()
            return redirect(url_for('login'))
        return render_template('register.html', form=form)


@app.route('/interface', methods=['GET'])
def interface_form():
    cur = db.conn.cursor(buffered=True)
    select_interface_name = "SELECT * FROM autotest_platform.interface;"
    cur.execute(select_interface_name)
    data = cur.fetchone()
    return render_template('interface.html', user=data[0], url=data[1], methods=data[2])


@app.route('/add_interface', methods=['POST','GET'])
def add_interface():
    add_interface_form = AddInterface()
    if add_interface_form.validate_on_submit():
        interface_name = request.form['interface_name']
        print type(interface_name)
        interface_url = request.form['interface_url']
        print type(interface_url)
        interface_method = request.form['interface_methods']
        print type(interface_method)
        cur = db.conn.cursor()
        cur.execute("insert into autotest_platform.interface (name,url,methods) values(%s,%s,%s)",(interface_name, interface_url, interface_method))
        db.conn.commit()
        return redirect(url_for('interface_form'))
    return render_template('add_interface.html', form = add_interface_form)


if __name__ == '__main__':
    app.run(debug=True)