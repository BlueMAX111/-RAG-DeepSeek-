import os
from dotenv import load_dotenv
# 自动加载 .env 变量
load_dotenv()

# 通用配置文件
class Config:
    # 配置 WTF 密钥
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '465'))
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'True')
    # MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False')   # QQ 邮箱填 False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    FLASK_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASK_MAIL_SENDER = 'Flask 超级管理员 <flask@example.com>'
    FLASK_ADMIN = os.getenv('FLASKY_ADMIN')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

# 开发环境配置文件
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')

# 测试环境配置文件
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')

# 生产环境配置文件
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

# 注册不同的配置环境，默认配置为开发环境
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}