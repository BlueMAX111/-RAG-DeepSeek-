from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask import flash, redirect, url_for

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
bootstrap = Bootstrap()
# 初始化用户会话验证扩展
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # 设置未登录时的重定向视图
login_manager.login_message = '请先登录账号'

