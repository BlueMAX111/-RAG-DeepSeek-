from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from . import auth
from app.models import db
from app.models import User
from .forms import LoginForm, RegistrationForm

# 登录功能实现
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()          # 创建表单
    if form.validate_on_submit():           #表单提交
        user = User.query.filter_by(email=form.email.data).first()      # 查找邮箱对应的用户
        if user is not None and user.verify_password(form.password.data):       # 验证用户密码
            login_user(user, form.remember_me.data)               #标记用户会话为登录
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            flash('登录成功', 'success')
            return redirect(next)
        flash('无效的邮箱地址或密码', 'success')

    return render_template('auth/login.html', form=form)

# 登出用户功能实现
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("登出用户账号成功")
    return redirect(url_for('main.index'))

# 注册用户功能实现
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password = form.password.data,
                    username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash("注册成功", "success")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)