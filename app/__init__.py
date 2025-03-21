from flask import Flask, render_template
from flask_moment import Moment
from config import config
from .extensions import db, migrate, mail, bootstrap, login_manager
from .models import User, Role

moment = Moment()

def create_app(config_name='default'):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)    #可以定义完成更复杂的初始化操作
    
    # 注册主蓝本
    from .blueprints.main import main as main_blueprints
    app.register_blueprint(main_blueprints) # 注册蓝图
    # 注册用户身份验证蓝本
    from .blueprints.auth import auth as auth_blueprints
    app.register_blueprint(auth_blueprints, url_prefix='/auth')

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @app.cli.command()
    def test():
        import unittest
        tests = unittest.TestLoader().discover('tests', pattern='test_send_email.py')
        unittest.TextTestRunner(verbosity=2).run(tests)

    return app

